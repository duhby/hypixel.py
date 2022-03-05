"""
The MIT License (MIT)

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

import asyncio
import json
from uuid import UUID
from collections import namedtuple
from datetime import datetime, timedelta

from typing import List
from typing import Optional
from typing import Union

import aiohttp

from . import utils
from .errors import *
from .models import *
from .utils import HashedDict

__all__ = (
    'Client',
)

class Client:
    """Main client object; interact with the API.

    .. note::

        :attr:`._keys` should not be modified directly due to internal
        errors that can occur. :meth:`.add_key` and :meth:`.remove_key`
        should be called instead.

    Parameters
    ----------
    keys: Optional[Union[:class:`str`, List[:class:`str`]]]
        Hypixel API key(s) the client will use to access the API.
    loop: Optional[:class:`asyncio.AbstractEventLoop`]
        The loop to use for asynchronous operations.
        Defaults to ``None``, in which case the event loop is created using
        :func:`asyncio.get_event_loop()`.
    autoclose: :class:`bool`
        Defaults to ``True``
    autoverify: :class:`bool`
        Defaults to ``False``
    handle_rate_limits: :class:`bool`
        Defaults to ``True``
    cache:
        Whether or not to cache (both mojang and hypixel, separately)
        api calls
        Defaults to ``False``
    cache_time:
        Amount of time until cached items expire
        Defaults to ``60``
    cache_size:
        Amount of recent unique calls to be stored in cache
        Defaults to ``None``

    Raises
    ------
    :exc:`.MalformedApiKey`
        Raised if an invalidly formed API key is passed.


    .. todo::
        Finish documentation for :class:`Client`.
    """
    def __init__(self, keys=None, *, loop=None, **options):
        self._keys = keys
        if self._keys is not None:
            if isinstance(self._keys, str):
                self._keys = [self._keys]
            elif not isinstance(self._keys, list):
                raise MalformedApiKey(self._keys)
            self._itr = iter(self._keys)
        else:
            self._itr = None
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.autoverify = options.get('autoverify', False)
        # self.rate_limit = options.get('rate_limit', True)
        self.cache = options.get('cache', False)
        self.cache_mojang = options.get('cache_mojang', self.cache)
        self.cache_hypixel = options.get('cache_hypixel', self.cache)
        # cache time

        self.cache_time = options.get('cache_time', 60)
        self.cache_time_m = options.get('cache_time_m', self.cache_time)
        self.cache_time_h = options.get('cache_time_h', self.cache_time)

        # cache size
        self.cache_size = options.get('cache_size', None)
        self.cache_size_m = options.get('cache_size_m', self.cache_size)
        self.cache_size_h = options.get('cache_size_h', self.cache_size)

        # internal
        self._session = aiohttp.ClientSession(loop=self.loop)

        # handle options
        if self.autoverify and self._keys:
            self.validate_keys()
        if self.cache_mojang:
            self._get_uuid = utils.async_timed_cache(
                self._get_uuid,
                self.cache_time_m,
                self.cache_size_m,
            )
        if self.cache_hypixel:
            self._get = utils.async_timed_cache(
                self._get,
                self.cache_time_h,
                self.cache_size_h,
            )

    # properties

    @property
    def keys(self) -> List[str]:
        return self._keys

    # remove these and use ._get.cache_info() instead? idk

    @property
    def hypixel_cache_info(self) -> Optional[namedtuple]:
        if self.cache is None:
            return None
        return self._get.cache_info()

    @property
    def mojang_cache_info(self) -> Optional[namedtuple]:
        if self.cache is None:
            return None
        return self._get_uuid.cache_info()

    # internal

    async def __aenter__(self):
        # open a new session if it has been closed
        if self._session.closed:
            self._session = aiohttp.ClientSession(loop=self.loop)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # don't return otherwise exceptions get suppressed
        await self._session.close()

    def _run(self, future):
        return self.loop.run_until_complete(future)

    def _next_key(self):
        if not self._keys:
            raise KeyRequired("'function' object '_next_key'")
        try:
            return next(self._itr)
        except StopIteration:
            self._itr = iter(self._keys)
            return next(self._itr)

    async def _get_uuid(self, name: str) -> str:
        if self._session.closed:
            raise ClosedSession
        response = await self._session.get(
            f'https://api.mojang.com/users/profiles/minecraft/{name}'
        )
        if response.status == 200:
            data = await response.json()
            uuid = data.get('id')
            if not uuid:
                raise PlayerNotFound(name) # for safety
            return uuid

        elif response.status == 204:
            raise PlayerNotFound(name)

        elif response.status == 429:
            # TODO: handle 429
            retry_after = None
            raise RateLimitError(retry_after, 'mojang', response)

        else:
            raise ApiError(response, 'mojang')

    async def _get_name(self, uuid: str) -> str:
        if self._session.closed:
            raise ClosedSession
        response = await self._session.get(
            f'https://api.mojang.com/user/profiles/{uuid}/names'
        )
        if response.status == 200:
            data = await response.json()
            name = data[-1].get('name')
            if not name:
                raise PlayerNotFound(uuid)
            return name

        elif response.status == 204:
            raise PlayerNotFound(uuid)

        elif response.status == 429:
            # TODO: handle 429
            # No Retry-After given
            retry_after = None
            raise RateLimitError(retry_after, 'mojang', response)

        else:
            raise ApiError(response, 'mojang')

    async def _get(
        self,
        path: str,
        *,
        # hashed to allow caching
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
        :exc:`.KeyRequired`
            Raised if no keys were passed and ``key_required=True``
        :exc:`.RateLimitError`.
            Raised if :attr:`.handle_rate_limits` is ``False`` and the rate
            limit was reached.
        :exc:`.InvalidApiKey`
            .
        :exc:`.ApiError`
            .
        :exc:`.ClosedSession`
            .

        .. todo::
            Finish documentation for :meth:`._get`
        """
        if self._session.closed:
            raise ClosedSession
        # TODO: handle 429
        if params is None:
            params = {}
        params = dict(params) # allow mutations

        if key:
            params['key'] = key
        elif key_required:
            if self._keys is None:
                raise KeyRequired(path)
            params['key'] = self._next_key()

        response = await self._session.get(
            f'https://api.hypixel.net/{path}',
            params=params,
        )
        if response.status == 200:
            return await response.json()

        elif response.status == 429:
            # TODO: handle 429
            retry_after = (
                datetime.now() +
                timedelta(seconds=int(response.headers['Retry-After']))
            )
            raise RateLimitError(retry_after, 'hypixel', response)

        elif response.status == 403:
            if params.get('key') is None:
                raise KeyRequired(path)
            raise InvalidApiKey(params['key'])

        else:
            try:
                text = await response.json()
                text = text.get('cause')
            except Exception:
                raise ApiError(response, 'hypixel')
            else:
                text = f'An unexpected error occurred with the hypixel API: {text}'
                raise ApiError(response, 'hypixel', text)

    # public

    async def close(self) -> None:
        """Safely close aiohttp session.

        .. note::

            This is here for if you want to handle the closing of the
            ClientSession by yourself if you are done using the object.
            An asynchronous context manager exists for if you want to use 
            ``async with`` to handle session cleanup automatically.

        .. warning::

            Make sure this is awaited before the program ends.

        .. warning::

            Calling a client method that requires an aiohttp session will
            raise a :exc:`.ClosedSession` exception.
        """
        await self._session.close()

    async def validate_keys(self) -> None:
        """Validate the keys passed into the client.

        .. note::

            This first checks for malformed UUIDs, and then requests
            key objects from the API to check if the keys are valid.
        """
        # check for malformed UUID
        for key in self._keys:
            try:
                UUID(key)
            except ValueError:
                raise MalformedApiKey(key)
        # check for invalid keys
        for key in self._keys:
            await self._get('key', key=key)

    def add_key(self, key: str) -> None:
        """Update :attr:`keys` and internal attributes."""
        if isinstance(key, str):
            self._keys.append(key)
            self._itr = iter(self._keys)
        else:
            raise MalformedApiKey(key)

    def remove_key(self, key: str) -> None:
        """Update :attr:`keys` and internal attributes."""
        if isinstance(key, str):
            self._keys.append(key)
            self._itr = iter(self._keys)
        else:
            raise MalformedApiKey(key)

    # Cache

    def clear_cache(self) -> None:
        """Clear hypixel and mojang lru caches."""
        if self.cache_mojang:
            self.clear_mojang_cache()
        if self.cache_hypixel:
            self.clear_hypixel_cache()

    def clear_mojang_cache(self) -> None:
        """Clear mojang lru cache."""
        if self.cache_mojang:
            self._get_uuid.clear_cache()

    def clear_hypixel_cache(self) -> None:
        """Clear hypixel lru cache."""
        if self.cache_hypixel:
            self._get.clear_cache()

    # API (mojang)

    async def get_uuid(self, name: str) -> str:
        """Get the uuid of a player."""
        if not isinstance(name, str):
            raise InvalidPlayerId(name)
        return await self._get_uuid(name)

    async def get_name(self, uuid: str) -> str:
        """Get the name of a player."""
        if not isinstance(uuid, str):
            raise InvalidPlayerId(uuid)
        return await self._get_name(uuid)

    # API (hypixel)

    @utils.convert_id
    async def player(self, id_: str) -> Player:
        """Create a :class:`Player` object based off an API response."""
        params = HashedDict(
            {'uuid': id_['uuid']}
        )
        response = await self._get('player', params=params)

        if not response.get('player'):
            raise PlayerNotFound(id_['orig'])

        data = {
            'raw': response,
            '_data': response['player']
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
            # make a new exception for HypixelException type errors
            raise HypixelException(
                f'TypeError: given key is not a string.'
            )
        try:
            UUID(key)
        except ValueError:
            raise MalformedApiKey(key)

        response = await self._get('key', key=key)

        if not response.get('record'):
            raise KeyNotFound(key)

        data = {
            'raw': response
        }
        clean_data = utils._clean(response['record'], mode='KEY')
        data.update(clean_data)
        return Key(**data)

    async def bans(self) -> Bans:
        """Get staff and watchdog ban info."""
        response = await self._get('watchdogstats')

        data = {
            'raw': response
        }
        clean_data = utils._clean(response, mode='BANS')
        data.update(clean_data)
        return Bans(**data)

    @utils.convert_id
    async def player_friends(self, id_: str) -> List[Friend]:
        """Get a list of a player's friends."""
        params = HashedDict(
            {'uuid': id_['uuid']}
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
            clean_data = utils._clean(friend, mode='FRIEND', extra=id_)
            data = raw.copy()
            data.update(clean_data)
            friends.append(Friend(**data))
        return friends

    @utils.convert_id
    async def player_status(self, id_: str) -> Status:
        """Get the status of a player."""
        params = HashedDict(
            {'uuid': id_['uuid']}
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
