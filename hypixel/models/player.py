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

from dataclasses import dataclass, fields, field
from datetime import datetime

from typing import Literal, Optional
from .games import GameType

from .. import utils

from .playerdata import Arcade
from .playerdata import Bedwars
from .playerdata import Duels
from .playerdata import Paintball
from .playerdata import Socials
from .playerdata import TurboKartRacers

__all__ = (
    'Player',
)

RankType = Literal[
    'VIP',
    'VIP+',
    'MVP',
    'MVP+',
    'MVP++',
    'YOUTUBE',
    'PIG+++',
    'MOJANG',
    'GAME MASTER',
    'ADMIN',
    'OWNER',
]

@dataclass
class Player:
    """Player model object.

    Attributes
    ----------
    rank: Optional[RankType]
        A string of the rank display if it exists, otherwise None.

    .. todo::

        Finish player class documentation.
    """
    _data: dict = field(repr=False)
    raw: dict = field(repr=False)
    id: str = None
    uuid: str = None
    first_login: datetime = None
    name: str = None
    last_login: datetime = None
    last_logout: datetime = None
    known_aliases: list = None
    # todo: change type to List[Achievement]
    achievements: list = field(default_factory=list, repr=False)
    achievements_multiple: dict = field(default_factory=dict, repr=False)
    network_exp: int = 0 # not sure why hypixel returns a float.. oh well
    karma: int = 0
    version: str = None
    achievement_points: int = 0
    current_gadget: str = None
    channel: str = None
    # require extra post init calculations
    rank: RankType = None
    level: float = None
    most_recent_game: GameType = None
    # gamemodes
    arcade: Arcade = field(init=False)
    bedwars: Bedwars = field(init=False)
    duels: Duels = field(init=False)
    paintball: Paintball = field(init=False)
    socials: Socials = field(init=False)
    tkr: TurboKartRacers = field(init=False)

    def __post_init__(self):
        # type conversion
        for date in ('first_login', 'last_login', 'last_logout'):
            value = getattr(self, date)
            if value is None:
                continue
            dt = utils.convert_to_datetime(value)
            setattr(self, date, dt)
        self.network_exp = int(self.network_exp)

        # extra post init calculations
        self.level = utils.get_level(self.network_exp)
        self.rank = utils.get_rank(self.raw)
        self.most_recent_game = utils.get_game_type(
            self.most_recent_game
        )

        # playerdata
        modes = {
            'arcade': Arcade,
            'bedwars': Bedwars,
            'duels': Duels,
            'paintball': Paintball,
            'socials': Socials,
            'tkr': TurboKartRacers,
        }
        for mode, model in modes.items():
            data = utils._clean(self._data, mode=mode.upper())
            setattr(self, mode, model(**data))
