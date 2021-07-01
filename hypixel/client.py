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
from typing import Union
from typing import Optional

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
        if self.keys:
            await self._validate_keys(self.keys)
        self.loop = asyncio.get_event_loop() if loop is None else loop
        # self.loop = options.get('loop', asyncio.get_event_loop())
        self.autoclose = options.get('autoclose', True)
        self.autoverify = options.get('autoverify', False)
        self.handle_429 = options.get('handle_429', True)

        # handle options
        if self.autoclose:
            atexit.register(self.close)
        if self.autoverify:
            self._run(self._validate_keys())

        # internal
        self._session = aiohttp.ClientSession(loop=self.loop)

    # internal

    def _run(self, future):
        self.loop.run_until_complete(future)

    async def _validate_keys(self, request=False):
        # check for malformed UUID
        for key in self.keys:
            try:
                uuid.UUID(key)
            except ValueError:
                raise(MalformedApiKey(key))
        if request:
            for key in self.keys:
                await self._get('key', key=key)

    async def _close(self):
        await self._session.close()

    async def _get(self, path, *, params=None, key=None):
        if params is None:
            params = {}
        pass

    def close(self):
        """Used for safely closing the aiohttp session."""
        self._run(self._close())
