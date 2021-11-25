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
from uuid import UUID
import atexit
import json
from datetime import datetime
from datetime import timedelta
from typing import Union
from typing import Optional
from typing import Dict
from typing import List

import aiohttp

from .errors import *
from .models import *
from . import utils

__all__ = (
    'Client',
)

class Client:
    """Main client object; used to interact with the API.

    .. note::

        :attr:`.keys` should not be modified directly due to internal
        errors that can occur. :meth:`.add_key` and :meth:`.remove_key`
        should be called instead.

    .. todo::

        Finish documentation for :class:`Client`.
    """
    def __init__(self, keys=None, *, loop=None, **options):
        self._keys = keys
        if self._keys:
            if isinstance(self._keys, str):
                self._keys = [self._keys]
            elif not isinstance(self._keys, list):
                raise MalformedApiKey(self._keys)
            self._itr = iter(self._keys)
        else:
            self._itr = None
        self.loop = asyncio.get_event_loop() if loop is None else loop
        # self.loop = options.get('loop', asyncio.get_event_loop())
        self.autoclose = options.get('autoclose', True)
        self.autoverify = options.get('autoverify', False)
        self.handle_rate_limits = options.get('handle_rate_limits', True)

        # handle options
        if self.autoclose:
            atexit.register(self.close)
        if self.autoverify and self._keys:
            self.validate_keys()

        # internal
        self._session = aiohttp.ClientSession(loop=self.loop)

    # properties

    @property
    def keys(self) -> List[str]:
        return self._keys

    # internal

    def _run(self, future):
        return self.loop.run_until_complete(future)

    def _next_key(self):
        if not self._keys:
            raise KeyRequired('_next_key()')
        try:
            return next(self._itr)
        except StopIteration:
            self._itr = iter(self._keys)
            return next(self._itr)

    async def _validate_keys(self):
        # check for malformed UUID
        for key in self._keys:
            try:
                uuid.UUID(key)
            except ValueError:
                raise(MalformedApiKey(key))
        # check for invalid keys
        for key in self._keys:
            await self._get('key', key_required=False, key=key)

    async def _close(self):
        await self._session.close()

    async def _get(
        self,
        path: str,
        *,
        params: Optional[Dict] = None,
        key_required: Optional[bool] = True,
        key: Optional[str] = None,
    ) -> Dict:
        """Retrieves raw data from hypixel.

        .. todo::

            Finish documentation for :meth:`._get`
        """
        # TODO: handle 429
        if params is None:
            params = {}

        if key_required:
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
            raise RateLimitError(retry_after, response)

        elif response.status == 403:
            if params.get('key') is None:
                raise KeyRequired(path)
            raise InvalidApiKey(params['key'])

        else:
            raise ApiError(response)

    def close(self) -> None:
        """Used for safely closing the aiohttp session.

        .. note::

            This is here for if you want to handle the closing of the
            ClientSession by yourself if you are done using the object.
            By default, this will be called when the script exits.
        """
        self._run(self._close())

    def validate_keys(self) -> None:
        """Validates the keys entered into the client.

        .. note::

            This first checks for malformed UUIDs, and then requests
            key objects from the API to check if the keys are valid.
        """
        self._run(self._validate_keys())

    def add_key(self, key: str) -> None:
        """Adds a key to :attr:`.keys` and updates internal attributes.
        """
        if isinstance(key, str):
            self._keys.append(key)
            self._itr = iter(self._keys)
        else:
            raise MalformedApiKey(key)

    def remove_key(self, key: str) -> None:
        """Removes a key from :attr:`.keys` and updates internal attributes.
        """
        if isinstance(key, str):
            self._keys.append(key)
            self._itr = iter(self._keys)
        else:
            raise MalformedApiKey(key)

    def player(self, id: str) -> Player:
        """Creates a :class:`Player` object based off an api response.
        """
        if not isinstance(id, str):
            raise TypeError('Given username or uuid is not a string.')
        try:
            UUID(id)
        except ValueError:
            try:
                uuid = self._run(utils._get_uuid(session=self._session, name=id))
            except ValueError:
                raise ValueError(f'Invalid username or uuid: {id}')                
        else:
            uuid = id

        params = {
            'uuid': uuid,
        }
        response = self._run(self._get('player', params=params))

        if not response['player']:
            raise PlayerNotFound(id)

        data = {
            'raw': response,
            '_data': response['player']
        }
        clean_data = utils._clean(response['player'])
        data.update(clean_data)
        return Player(**data)
