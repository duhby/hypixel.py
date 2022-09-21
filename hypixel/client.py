"""
The MIT License

Copyright (c) 2021-present duhby

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import sys
import asyncio
import json
from uuid import UUID
from collections import namedtuple
from operator import attrgetter

from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import aiohttp

from . import utils
from .errors import *
from .models import *
from .utils import ExponentialBackoff, HashedDict

try:
    import ujson
    JSON_DECODER = ujson.loads
except ImportError:
    JSON_DECODER = json.loads

__all__ = (
    'Client',
)

class Client:
    """Class for interacting with both the Mojang and Hypixel APIs.

    Parameters
    ----------
    keys: Union[:class:`str`, List[:class:`str`]]
        The Hypixel API key(s) the client will use to access the API.

        .. warning::

            :exc:`KeyRequired` will be raised if a method is called that requires an API
            key and none were passed or added with :meth:`add_key`.
    loop: :class:`asyncio.AbstractEventLoop`
        The loop the client will use for asynchronous operations.
        Defaults to ``None`` in which case the event loop is created using
        :func:`asyncio.get_event_loop()`.
    autoverify: :class:`bool`
        Runs :meth:`validate_keys` on client initialization.
        Defaults to ``False``.
    cache: :class:`bool`
        Whether or not API calls are cached. If ``True``, new requests won't be made for
        the same calls to request methods if the response for the passed arguments is
        still stored.
        Defaults to ``False``.

        .. note::

            Cached items will be stored either until the size limit is reached
            (``self.cache_size``), or the cached data expires (``self.cache_time``).

        .. note::

            The cache uses an async, time-invalidating, least recently used
            implementation. This means it works on asynchronous functions, can invalidate
            items that have been in the cache for x amount of time, and can remove least
            recently used items if the size limit is reached.

        .. admonition:: Limitations

            When a cached item is time-invalidated, it does not get removed from the
            cache and can inflate the cache size with multiple of the same item if they
            were called far enough apart from each other and ``self.cache_time`` is not
            ``None``. ``self.cache_time`` is based on the time from when it's first added
            to the cache, and not refreshed on the last access to that cached item. This
            could also be considered a feature and is therefore a design decision.
    cache_h: :class:`bool`
        Whether or not to cache Hypixel API calls.
        Refer to ``self.cache`` for more information.
        Defaults to ``self.cache``.
    cache_m: :class:`bool`
        Whether or not to cache Mojang API calls.
        Refer to ``self.cache`` for more information.
        Defaults to ``self.cache``.
    cache_size: :class:`int`
        The amount of cached items that are stored before deleting the oldest items.
        If ``None`` (the default), then there is no limit.
    cache_size_h: :class:`int`
        Cache size for the Hypixel API.
        Refer to ``self.cache_size`` for more information.
        Defaults to ``self.cache_size``.
    cache_size_m: :class:`int`
        Cache size for the Mojang API.
        Refer to ``self.cache_size`` for more information.
        Defaults to ``self.cache_size``.
    cache_time: :class:`int`
        The amount of time (in seconds) cached items can be stored before getting
        invalidated.
        Defaults to ``60``.

        .. note::

            The timestamp of a cached item is stored when the function is called, not when
            it is returned. So, the time the API takes to get the request counts towards
            the time invalidation. That's why it's recommended to have a value of at least
            10, but for the average use case it should be at least 60 if you want to get
            any cache hits.
    cache_time_h: :class:`int`
        Cache time for the Hypixel API. Refer to ``self.cache_time`` for more information.
        Defaults to ``self.cache_time``.
    cache_time_m: :class:`int`
        Cache time for the Mojang API. Refer to ``self.cache_time`` for more information.
        Defaults to ``self.cache_time``.
    rate_limit: :class:`bool`
        Whether or not to handle rate limits.
        Defaults to ``True``.

        .. note::

            For the Hypixel API, this will wait for the 'Retry-After' header amount of
            time either until a non-429 status is returned, or 'Retry-After' exceeds
            ``self.timeout``.

        .. note::

            For the Mojang API, this will wait for :func:`ExponentialBackoff.delay`
            amount of time either until a non-429 status is returned, or the time from
            the last invocation exceeds ``self.timeout`` in which case :exc:`TimeoutError`
            is raised. The delay time is reset on every new Mojang method call.
    rate_limit_h: :class:`bool`
        Whether or not to handle Hypixel API rate limits.
        See ``self.rate_limit`` for more information.
        Defaults to ``self.rate_limit``.
    rate_limit_m: :class:`bool`
        Whether or not to handle Mojang API rate limits.
        See ``self.rate_limit`` for more information.
        Defaults to ``self.rate_limit``.
    timeout: :class:`int`
        The maximum amount of time (in seconds) to wait for a request.
        This includes both waiting for a request to return, and waiting for rate limit
        retry times if ``self.rate_limit`` is ``True``.
        Defaults to ``10``.

        .. warning::

            ``None`` *is* a valid argument; however, it is highly advised against using
            because there's no fallback without a timeout, and there are chances you
            might end up waiting a very long time.

        .. warning::

            If ``self.rate_limit`` is ``True`` (default), then for Mojang API requests, if
            a 429 response is received and the interval is greater than ``self.timeout``,
            then it will raise a :exc:`TimeoutError`.

    Raises
    ------
    LoopPolicyError
        Raised when the event loop policy is misconfigured.
    MalformedApiKey
        Raised when an invalidly formed API key is passed.
    """
    def __init__(self, keys=None, *, loop=None, **options):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        try:
            if (
                isinstance(
                    asyncio.get_event_loop_policy(),
                    asyncio.DefaultEventLoopPolicy,
                )
                and sys.version_info[0] == 3
                and sys.version_info[1] >= 8
                and sys.platform.startswith('win')
            ):
                raise LoopPolicyError
        except AttributeError:
            pass

        self._keys = keys
        if self._keys is not None:
            if isinstance(self._keys, str):
                self._keys = [self._keys]
            elif not isinstance(self._keys, list):
                raise MalformedApiKey(self._keys)
            self._itr = iter(self._keys)
        else:
            self._itr = None

        self.autoverify = options.get('autoverify', False)
        self.timeout = options.get('timeout', 10)

        self.cache = options.get('cache', False)
        self.cache_h = options.get('cache_h', self.cache)
        self.cache_m = options.get('cache_m', self.cache)

        self.cache_size = options.get('cache_size', None)
        self.cache_size_h = options.get('cache_size_h', self.cache_size)
        self.cache_size_m = options.get('cache_size_m', self.cache_size)

        self.cache_time = options.get('cache_time', 60)
        self.cache_time_h = options.get('cache_time_h', self.cache_time)
        self.cache_time_m = options.get('cache_time_m', self.cache_time)

        self.rate_limit = options.get('rate_limit', True)
        self.rate_limit_h = options.get('rate_limit_h', self.rate_limit)
        self.rate_limit_m = options.get('rate_limit_m', self.rate_limit)

        # self._session = options.get('session', None)
        # if self._session is None:
        self._session = aiohttp.ClientSession(
            loop=self.loop,
            timeout=aiohttp.ClientTimeout(
                total=self.timeout,
            ),
        )

        if self.autoverify and self._keys:
            self.validate_keys()
        if self.cache_h:
            self._get = utils.async_timed_cache(
                self._get,
                self.cache_time_h,
                self.cache_size_h,
            )
        if self.cache_m:
            self._get_uuid = utils.async_timed_cache(
                self._get_uuid,
                self.cache_time_m,
                self.cache_size_m,
            )
            self._get_name = utils.async_timed_cache(
                self._get_name,
                self.cache_time_m,
                self.cache_size_m,
            )

    @property
    def keys(self) -> List[str]:
        """List[:class:`str`]: A list of Hypixel API key(s) that were passed or added
        to the client.

        Can also be ``None``.
        """
        return self._keys

    @property
    def hypixel_cache_info(self) -> Optional[namedtuple]:
        """:class:`type`: A named tuple that represents cache information for all Hypixel
        API related methods.

        This is the same as ``functools.lru_cache.cache_info()``.
        Fields are ``hits``, ``misses``, ``maxsize``, and ``currsize``. All of which are
        an :class:`int` except ``maxsize`` which can also be ``None``.
        """
        if self.cache is None:
            return None
        return self._get.cache_info()

    @property
    def mojang_cache_info(self) -> Optional[namedtuple]:
        """:class:`type`: A named tuple that represents cache information for all Mojang
        related methods.

        This is the same as ``functools.lru_cache.cache_info()``.
        Fields are ``hits``, ``misses``, ``maxsize``, and ``currsize``. All of which are
        an :class:`int` except ``maxsize`` which can also be ``None``.
        """
        if self.cache is None:
            return None
        return self._get_uuid.cache_info()

    async def __aenter__(self):
        # Open a new session if it has been closed
        if self._session.closed:
            self._session = aiohttp.ClientSession(loop=self.loop)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # Await but don't return
        # If a truthy value is returned, it suppresses exceptions
        await self._session.close()

    # def _run(self, future):
    #     return self.loop.run_until_complete(future)

    def _next_key(self):
        if not self._keys:
            raise KeyRequired("method '_next_key'")
        try:
            return next(self._itr)
        except StopIteration:
            self._itr = iter(self._keys)
            return next(self._itr)

    async def _get_uuid_helper(self, name):
        return await self._session.get(
            f'https://api.mojang.com/users/profiles/minecraft/{name}'
        )

    async def _get_uuid(self, name: str) -> str:
        if self._session.closed:
            raise ClosedSession
        try:
            response = await self._get_uuid_helper(name)
        except asyncio.TimeoutError:
            raise TimeoutError('mojang')

        if response.status == 429:
            if not self.rate_limit_m:
                retry_after = None
                raise RateLimitError(retry_after, 'mojang', response)
            else:
                while response.status == 429:
                    backoff = ExponentialBackoff(self.timeout)
                    retry = backoff.delay()
                    await asyncio.sleep(retry)
                    response = await self._get_uuid_helper(name)

        if response.status == 200:
            data = await response.json(loads=JSON_DECODER)
            uuid = data.get('id')
            if not uuid:
                raise PlayerNotFound(name)
            return uuid

        elif response.status == 204:
            raise PlayerNotFound(name)

        else:
            raise ApiError(response, 'mojang')

    async def _get_name_helper(self, uuid):
        return await self._session.get(
            f'https://api.mojang.com/user/profile/{uuid}'
        )

    async def _get_name(self, uuid: str) -> str:
        if self._session.closed:
            raise ClosedSession
        try:
            response = await self._get_name_helper(uuid)
        except asyncio.TimeoutError:
            raise TimeoutError('mojang')

        if response.status == 429:
            if not self.rate_limit_m:
                retry_after = None
                raise RateLimitError(retry_after, 'mojang', response)
            else:
                while response.status == 429:
                    backoff = ExponentialBackoff(self.timeout)
                    retry = backoff.delay()
                    await asyncio.sleep(retry)
                    response = await self._get_name_helper(uuid)

        if response.status == 200:
            data = await response.json(loads=JSON_DECODER)
            name = data.get('name')
            if not name:
                raise PlayerNotFound(uuid)
            return name

        elif response.status == 204:
            raise PlayerNotFound(uuid)

        else:
            print(response.status)
            raise ApiError(response, 'mojang')

    async def _get_helper(self, path, params):
        return await self._session.get(
            f'https://api.hypixel.net/{path}',
            params=params,
        )

    async def _get(
        self,
        path: str,
        *,
        # Hashed to allow caching
        params: Optional[HashedDict] = None,
        key_required: Optional[bool] = True,
        key: Optional[str] = None,
    ) -> dict:
        """Retrieve raw data from hypixel.

        Parameters
        ----------
        path: str
            The API path to request from.
        params: Optional[:class:`HashedDict`]
            Parameters to give the API.
        key_required: Optional[bool]
            If an API key is required to process the request.
        key: Optional[str]
            To use a specific key.

        Raises
        ------
        :exc:`KeyRequired`
            Raised if no keys were passed and ``key_required=True``
        :exc:`RateLimitError`.
            Raised if ``self.rate_limit_h`` is ``False`` and the rate limit was reached.
        :exc:`InvalidApiKey`
            .
        :exc:`ApiError`
            .
        :exc:`ClosedSession`
            .
        """
        if self._session.closed:
            raise ClosedSession
        if params is None:
            params = {}
        params = dict(params) # Allow mutations

        if key:
            params['key'] = key
        elif key_required:
            if self._keys is None:
                raise KeyRequired(path)
            params['key'] = self._next_key()

        try:
            response = await self._get_helper(path, params)
        except asyncio.TimeoutError:
            raise TimeoutError('hypixel')

        if response.status == 429:
            if not self.rate_limit_h:
                # Initially <class 'str'>
                retry_after = int(response.headers['Retry-After'])
                raise RateLimitError(retry_after, 'hypixel', response)
            else:
                while response.status == 429:
                    # Retrying exactly after the amount of seconds can
                    # cause spamming the API while still being limited
                    # because the time is restricted to int precision.
                    retry = int(response.headers['Retry-After']) + 1
                    if self.timeout is not None and retry > self.timeout:
                        raise TimeoutError('hypixel')
                    await asyncio.sleep(retry)
                    response = await self._get_helper(path, params)

        if response.status == 200:
            return await response.json(loads=JSON_DECODER)

        elif response.status == 403:
            if params.get('key') is None:
                raise KeyRequired(path)
            raise InvalidApiKey(params['key'])

        else:
            try:
                text = await response.json(loads=JSON_DECODER)
                text = text.get('cause')
            except Exception:
                raise ApiError(response, 'hypixel')
            else:
                text = f'An unexpected error occurred with the hypixel API: {text}'
                raise ApiError(response, 'hypixel', text)

    # Public

    async def close(self) -> None:
        """Safely close the aiohttp session.

        .. note::

            This is here for if you want to handle the closing of the
            ``self.ClientSession`` by yourself if you are done using the Client. You can
            also use the Client with an asynchronous context manager (``async with``) if
            you want to handle session cleanup automatically.

        .. warning::

            Make sure this is awaited before the program ends if you aren't using a
            context manager.

        .. warning::

            Calling a client method that requires an open aiohttp session after this is
            called will raise a :exc:`ClosedSession` exception.
        """
        await self._session.close()

    async def validate_keys(self) -> None:
        """Validate the keys passed into the client.

        .. note::

            This first checks for malformed UUIDs, and then requests key objects from the
            API to check if the keys are valid.

        .. note::

            An error is raised when the first invalid key is found, so this is not
            viable for testing all of your keys at once if more than one is invalid.
        """
        for key in self._keys:
            try:
                UUID(key)
            except ValueError:
                raise MalformedApiKey(key)
        for key in self._keys:
            await self._get('key', key=key)

    def add_key(self, key: str) -> None:
        """Add a key to ``self.keys`` and update internal attributes.

        Parameters
        ----------
        key: :class:`str`
            The Hypixel API key to add to the Client.
        """
        if isinstance(key, str):
            self._keys.append(key)
            self._itr = iter(self._keys)
        else:
            raise MalformedApiKey(key)

    def remove_key(self, key: str) -> None:
        """Remove a key from ``self.keys`` and update internal attributes.

        Parameters
        ----------
        key: :class:`str`
            The Hypixel API key to remove from the Client.
        """
        if isinstance(key, str):
            try:
                self._keys.remove(key)
                self._itr = iter(self._keys)
            except ValueError:
                pass
        else:
            raise MalformedApiKey(key)

    # Cache

    def clear_cache(self) -> None:
        """Clear hypixel and mojang caches."""
        if self.cache_m:
            self.clear_mojang_cache()
        if self.cache_h:
            self.clear_hypixel_cache()

    def clear_mojang_cache(self) -> None:
        """Clear mojang cache."""
        if self.cache_m:
            self._get_uuid.clear_cache()

    def clear_hypixel_cache(self) -> None:
        """Clear hypixel cache."""
        if self.cache_h:
            self._get.clear_cache()

    # API (Mojang)

    async def get_uuid(self, name: str) -> str:
        """Get the uuid of a player from their username.

        Parameters
        ----------
        name: :class:`str`
            The username of the player.

        Raises
        ------
        ApiError
            An unexpected error occurred with the Mojang API.
        ClosedSession
            ``self.ClientSession`` is closed.
        InvalidPlayerId
            The passed player name is not a string.
        PlayerNotFound
            The passed player name does not exist.
        RateLimitError
            The rate limit is exceeded and ``self.rate_limit_m`` is ``False``.
        TimeoutError
            The request took longer than ``self.timeout``, or the retry delay time is
            longer than ``self.timeout``.

        Returns
        -------
        :class:`str`
            The uuid of the player.
        """
        if not isinstance(name, str):
            raise InvalidPlayerId(name)
        return await self._get_uuid(name)

    async def get_name(self, uuid: str) -> str:
        """Get the username of a player from their uuid.

        Parameters
        ----------
        uuid: :class:`str`
            The uuid of the player.

        Raises
        ------
        ApiError
            An unexpected error occurred with the Mojang API.
        ClosedSession
            ``self.ClientSession`` is closed.
        InvalidPlayerId
            The passed player uuid is not a string.
        PlayerNotFound
            The passed player uuid does not exist.
        RateLimitError
            The rate limit is exceeded and ``self.rate_limit_m`` is ``False``.
        TimeoutError
            The request took longer than ``self.timeout``, or the retry delay time is
            longer than ``self.timeout``.

        Returns
        -------
        :class:`str`
            The name of the player.
        """
        if not isinstance(uuid, str):
            raise InvalidPlayerId(uuid)
        return await self._get_name(uuid)

    # API (Hypixel)

    @utils.convert_id
    async def player(self, id_: str) -> Player:
        """Create a player model from the API response from the player id.

        Parameters
        ----------
        id\_: :class:`str`
            The username or uuid of a player.

        Raises
        ------
        ApiError
            An unexpected error occurred with the Hypixel API.
        ClosedSession
            ``self.ClientSession`` is closed.
        InvalidApiKey
            The API key used is invalid.
        KeyRequired
            The client does not have any keys.
        PlayerNotFound
            The passed player id does not exist in Mojang's or Hypixel's databases.
        RateLimitError
            The rate limit is exceeded and ``self.rate_limit_h`` is ``False``.
        TimeoutError
            The request took longer than ``self.timeout``, or the retry delay time is
            longer than ``self.timeout``.

        Returns
        -------
        Player
            The player model used to abstract data.
        """
        params = HashedDict(
            uuid=id_['uuid']
        )
        response = await self._get('player', params=params)

        if not response.get('player'):
            raise PlayerNotFound(id_['orig'])

        data = {
            'raw': response,
            '_data': response['player'],
        }
        clean_data = utils._clean(response['player'], mode='PLAYER')
        data.update(clean_data)
        return Player(**data)

    async def player_count(self) -> int:
        """Get the number of players online."""
        response = await self._get('playerCount')

        return int(response['playerCount'])

    async def key(self, key: str) -> Key:
        """Get the data of a key."""
        if not isinstance(key, str):
            raise ArgumentError(
                f"Given key '{key}' is not a string."
            )
        try:
            UUID(key)
        except ValueError:
            raise MalformedApiKey(key)

        response = await self._get('key', key=key)

        if not response.get('record'):
            raise KeyNotFound(key)

        data = {
            'raw': response,
        }
        clean_data = utils._clean(response['record'], mode='KEY')
        data.update(clean_data)
        return Key(**data)

    async def bans(self) -> Bans:
        """Get staff and watchdog ban info."""
        response = await self._get('watchdogstats')

        data = {
            'raw': response,
        }
        clean_data = utils._clean(response, mode='BANS')
        data.update(clean_data)
        return Bans(**data)

    @utils.convert_id
    async def player_friends(self, id_: str, sort=False) -> List[Friend]:
        """Get a list of a player's friends."""
        params = HashedDict(
            uuid=id_['uuid']
        )
        response = await self._get('friends', params=params)

        if not response.get('records'): # probably has no friends
            raise PlayerNotFound(id_['orig'])

        records = response['records']

        raw = {
            'raw': response,
        }

        friends = []
        for friend in records:
            clean_data = utils._clean(friend, mode='FRIEND', extra=id_['uuid'])
            data = raw.copy()
            data.update(clean_data)
            friends.append(Friend(**data))

        if sorted:
            # Faster than lambda
            friends = sorted(friends, key=attrgetter('started'))
        return friends

    @utils.convert_id
    async def player_status(self, id_: str) -> Status:
        """Get the status of a player."""
        params = HashedDict(
            uuid=id_['uuid']
        )
        response = await self._get('status', params=params)

        if not response.get('session'):
            raise PlayerNotFound(id_['orig'])

        session = response['session']

        data = {
            'raw': response,
        }
        clean_data = utils._clean(session, mode='STATUS')
        data.update(clean_data)
        return Status(**data)

    async def guild_by_id(self, id_: str) -> Guild:
        """Get a guild from the id."""
        params = HashedDict(
            id=id_
        )
        response = await self._get('guild', params=params)

        if not response.get('guild'):
            raise GuildNotFound(id_)

        data = {
            'raw': response,
        }
        clean_data = utils._clean(response['guild'], mode='GUILD')
        data.update(clean_data)
        return Guild(**data)

    @utils.convert_id
    async def guild_by_player(self, id_: str) -> Guild:
        """Get a guild from a player."""
        params = HashedDict(
            player=id_['uuid']
        )
        response = await self._get('guild', params=params)

        if not response.get('guild'):
            raise GuildNotFound(id_['orig'])

        data = {
            'raw': response,
        }
        clean_data = utils._clean(response['guild'], mode='GUILD')
        data.update(clean_data)
        return Guild(**data)

    async def guild_by_name(self, name: str) -> Guild:
        """Get a guild from the name."""
        params = HashedDict(
            name=name
        )
        response = await self._get('guild', params=params)

        if not response.get('guild'):
            raise GuildNotFound(name)

        data = {
            'raw': response,
        }
        clean_data = utils._clean(response['guild'], mode='GUILD')
        data.update(clean_data)
        return Guild(**data)

    async def leaderboards(self) -> Dict[str, List[Leaderboard]]:
        """Get the game leaderboards."""
        response = await self._get('leaderboards')

        if not response.get('leaderboards'):
            raise ApiError(response, 'hypixel')

        leaderboards = {}
        for mode, values in response['leaderboards'].items():
            lbs = []
            for lb in values:
                data = utils._clean(lb, mode='LB')
                lbs.append(Leaderboard(**data))
            leaderboards[mode] = lbs

        return leaderboards

        # leaderboards = []
        # for mode in response['leaderboards'].values():
        #     for lb in mode:
        #         data = utils._clean(lb, mode='LB')
        #         leaderboards.append(Leaderboard(**data))

        # leaderboards = {}
        # for mode, data in response['leaderboards'].items():
        #     leaderboards[mode] = GameLeaderboard(_data=data)

        # return leaderboards
