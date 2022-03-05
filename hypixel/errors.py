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

from __future__ import annotations
from typing import Any

__all__ = (
    'HypixelException',
    'InvalidPlayerId',
    'PlayerNotFound',
    'KeyNotFound',
    'ApiError',
    'RateLimitError',
    'InvalidApiKey',
    'MalformedApiKey',
    'KeyRequired',
    'ClosedSession',
)

class HypixelException(Exception):
    """Base exception for hypixel.py

    Theoretically, this can be used to catch all errors from this library.
    """

class InvalidPlayerId(HypixelException):
    """Raised when a passed player id does not have a string value.

    Inherits from :exc:`HypixelException`

    Attributes
    ----------
    id: str
        The invalid player id.
    text: str
        The text of the error.
    """
    def __init__(self, player_id):
        self.id = player_id
        self.text = f"Passed player id '{self.id}' is not a string"
        super().__init__(self.text)

class PlayerNotFound(HypixelException):
    """Raised when a requested player does not exist.

    Inherits from :exc:`HypixelException`

    Attributes
    ----------
    player: str
        The player requested. Could be a UUID or a username.
    text: str
        The text of the error.
    """
    def __init__(self, player):
        self.player = player
        self.text = f"Player '{self.player}' did not yield a response"
        super().__init__(self.text)

class KeyNotFound(HypixelException):
    """Raised when a requested key does not exist.

    Inherits from :exc:`HypixelException`

    Attributes
    ----------
    key: str
        The key requested.
    text: str
        The text of the error.
    """
    def __init__(self, key):
        self.key = key
        self.text = f"Key '{self.key}' did not yield a response"
        super().__init__(self.text)

class ApiError(HypixelException):
    """Base exception for when an API request fails.

    Inherits from :exc:`HypixelException`

    Attributes
    ----------
    api: str
        The API that caused the error.
    response: aiohttp.ClientResponse
        The client response object that was received.
    text: str
        The text of the error.
    """
    def __init__(self, response, api, message=None):
        if message is None:
            message = f"An unknown error occured with the {api} API"
        self.api = api
        self.text = message
        self.response = response
        super().__init__(self.text)

class RateLimitError(ApiError):
    """Raised when the rate limit is reached.

    Inherits from :exc:`ApiError`

    .. note::

        Will not be raised if :attr:`Client.handle_rate_limits` is
        ``True`` (default).

    Attributes
    ----------
    retry_after: datetime.datetime
        The time to wait until to retry a request.
    text: str
        The text of the error.
    """
    def __init__(self, retry_after, api, response):
        self.retry_after = retry_after
        if retry_after is None:
            self.text = f"You are being rate limited ({api})"
        else:
            self.text = (
                "You are being rate limited, "
                f"try again at {self.retry_after.strftime('%H:%M:%S')}"
            )
        super().__init__(response, api, message=self.text)

class InvalidApiKey(HypixelException):
    """Base exception for invalid API key exceptions.

    Inherits from :exc:`HypixelException`

    .. note::

        Will not be raised until a request is made unless the key is
        malformed or :meth:`Client.validate_keys` is called.

    .. warning::

        For simplicity, if multiple API keys are invalid, only the first
        one will be included, even if :meth:`Client.validate_keys` is
        called multiple times with the same keys.

    Attributes
    ----------
    key: str
        The key that caused the error to be raised.
    text: str
        The text of the error.
    """
    def __init__(self, key, message=None):
        if message is None:
            message = "API key is not valid"
        self.text = message
        self.key = key
        super().__init__(self.text)

class MalformedApiKey(InvalidApiKey, ValueError):
    """Raised when a passed API key is not in valid UUID
    format.

    Inherits from :exc:`InvalidApiKey` and :exc:`ValueError`

    Attributes
    ----------
    key: str
        The key that caused the error to be raised. See
        :exc:`InvalidApiKey` for details.
    text: str
        The text of the error.
    """
    def __init__(self, key):
        self.text = "API key is not a valid uuid string"
        super().__init__(key, self.text)

class KeyRequired(InvalidApiKey, TypeError):
    """Raised when an API key is required but none were
    passed.

    Inherits from :exc:`InvalidApiKey` and :exc:`TypeError`

    Attributes
    ----------
    path: str
        The path that caused the error.
    text: str
        The text of the error.
    """
    def __init__(self, path):
        self.path = path
        self.text = f"{self.path} requires an API key to be used"
        super().__init__(None, self.text)

class ClosedSession(HypixelException, RuntimeError):
    """Raised when the Client tries to make an API call
    after :meth:`Client.close` is called.

    Inherits from :exc:`HypixelException` and :exc:`RuntimeError`

    .. note::

        If :attr:`Client.cache` is ``True`` and the response is stored in
        cache, :exc:`ClosedSession` won't be raised and the function will
        return normally.
    """
    def __init__(self):
        self.text = 'Session is closed'
        super().__init__(self.text)
