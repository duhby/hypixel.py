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
import uuid
import atexit
import json
from datetime import datetime
from datetime import timedelta
from typing import Union
from typing import Optional
from typing import Dict

import aiohttp

from .errors import *
from .models import *
from . import utils

__all__ = (
    'Client',
)

class Client:
    """Main client object; used to interact with the API.
    
    .. todo::
    
        Finish documentation for :class:`Client`.
    """
    def __init__(self, keys=None, *, loop=None, **options):
        self.keys = keys
        self.itr = None
        if self.keys:
            if isinstance(self.keys, str):
                self.keys = [self.keys]
            elif not isinstance(self.keys, list):
                raise MalformedApiKey(self.keys)
            self.itr = iter(self.keys)
        self.loop = asyncio.get_event_loop() if loop is None else loop
        # self.loop = options.get('loop', asyncio.get_event_loop())
        self.autoclose = options.get('autoclose', True)
        self.autoverify = options.get('autoverify', False)
        self.handle_429 = options.get('handle_429', True)

        # handle options
        if self.autoclose:
            atexit.register(self.close)
        if self.autoverify and self.keys:
            self._run(self._validate_keys())

        # internal
        self._session = aiohttp.ClientSession(loop=self.loop)

    # internal

    def _run(self, future):
        self.loop.run_until_complete(future)

    def _next_key(self):
        if self.itr is None:
            raise KeyRequired('_next_key()')
        try:
            return next(self.itr)
        except StopIteration:
            itr = iter(self.keys)
            return next(self.itr)

    async def _validate_keys(self, request=False):
        # check for malformed UUID
        for key in self.keys:
            try:
                uuid.UUID(key)
            except ValueError:
                raise(MalformedApiKey(key))
        if request:
            for key in self.keys:
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
            if self.keys is None:
                raise KeyRequired(path)
            params['key'] = self._next_key()

        response = await self._session.get(
            f'https://api.hypixel.net/{path}',
            params=params,
        )

        if response.status == 200:
            data = await response.json()
            return {
                'data': data,
                'response': response,
            }

        elif response.status == 429:
            # TODO: handle 429
            retry_after = datetime.now() + timedelta(seconds=int(response.headers['Retry-After']))
            raise RateLimitError(retry_after, response)

        elif response.status == 403:
            if params.get('key') is None:
                raise KeyRequired(path)
            raise InvalidApiKey(params['key'])

        else:
            raise ApiError(response)

    def close(self):
        """Used for safely closing the aiohttp session."""
        self._run(self._close())
