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
    """Base exception for invalid API key exceptions.

    .. note::

        Will not be raised until a request is made unless the key is malformed or 
        :meth:`Client.validate_keys` is called.

    .. warning::

        If multiple API keys are invalid, only the first key will be included.

    Attributes
    ----------
    key: str
        The key(s) that caused the error to be raised.
    text: str
        
    """
    def __init__(self, key, message=None):
        if message is None:
            message = "API key is not valid"
        self.text = message
        self.key = key
        super().__init__(self.text)

class MalformedApiKey(InvalidApiKey, ValueError):
    """Exception that is raised when a passed API key is not in valid UUID format.

    Subclass of :exc:`InvalidApiKey`

    .. todo::

        Finish documentation for :class:`MalformedApiKey`.
    """
    def __init__(self, key: str, message: str = None) -> None:
        if message is None:
            message = "API key is not a valid uuid string"
        self.text = message
        super().__init__(key, self.text)
