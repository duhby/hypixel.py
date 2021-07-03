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

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from typing import List
from typing import Dict
from typing import Any

from .. import utils

from .games import *
from . import Socials
from . import Achievement
from . import Game
from . import Parkour

__all__ = (
    Player,
)

@dataclass
class Player:
    _data: Dict[str, Any]
    raw: Dict[str, Any]
    id: str
    uuid: str
    first_login: datetime
    name: str
    last_login: datetime = None
    last_logout: datetime = None
    known_aliases: List[str] = None
    achievements: List[Achievement] = None
    network_exp: int = 0
    karma: int = 0
    version: str = None
    achievement_points: int = 0
    current_gadget: str = None
    channel: str = None
    most_recent_game: Game = None

    def __post_init__(self):
        # stats - use individual games instead of one stats class
        # stats = utils._clean(self._data, mode='stats')
        # stats['_data'] = self._data
        # self.stats: Stats = Stats(**stats)

        # level
        self.level: float = utils.get_level(self.network_exp)

        # socials
        socials = utils._clean(self._data, mode='socials')
        self.socials: Socials = Socials(**socials)

        # parkour
        parkour = utils._clean(self._data, mode='parkour')
        self.parkour: Parkour = Parkour(**parkour)
