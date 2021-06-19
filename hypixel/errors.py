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

import uuid
from client import Client
from typing import List

__all__ = (
    'HypixelException',
    'InvalidApiKey',
)

class HypixelException(Exception):
    """Base exception for hypixel.py

    Theoretically, this can be used to catch all errors from this library.
    """
    pass

class InvalidApiKey(HypixelException):
    """An exception that is raised when an invalid API key is passed into :class:`Client`

    .. note::

        Will not be raised until a request is made if the key is invalid
        and properly formatted.

    Attributes
    ----------
    keys: List[:class:`uuid.UUID`]
        The key(s) that caused the error to be raised.

    .. note::

        If multiple keys are invalid, ``keys`` will only contain
        all the invalid keys if any of the following are true:
            - the keys are malformed
            - :meth:`Client.validate_keys` is called
        Otherwise, only the key that caused the error will be included.
    """
    def __init__(self, keys: List[uuid.UUID], message: str = "Invalid API Key") -> None:
        self.message = message
        self.keys = keys
        super().__init__(self.message)
