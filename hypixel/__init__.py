"""
hypixel.py
~~~~~~~~~~

A python wrapper for the Hypixel API

Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

__title__ = 'hypixel'
__author__ = 'duhby'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present duhby'
__version__ = 'dev'

from .client import *
from .color import *
from .errors import *
from .models import *
from .game import *
from .utils import ExponentialBackoff, HashedDict

from typing import NamedTuple, Literal


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int

version_info: VersionInfo = VersionInfo(
    major=0,
    minor=3,
    micro=1,
    releaselevel='alpha',
    serial=0,
)

del NamedTuple, Literal, VersionInfo
