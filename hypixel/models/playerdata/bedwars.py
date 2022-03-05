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

from dataclasses import dataclass, fields, field
from ... import utils

@dataclass
class BedwarsMode:
    kills: int = 0
    deaths: int = 0
    wins: int = 0
    losses: int = 0
    games_played: int = 0
    final_kills: int = 0
    final_deaths: int = 0
    beds_broken: int = 0
    beds_lost: int = 0

    @property
    def kdr(self) -> float:
        return utils.safe_div(self.kills, self.deaths)

    @property
    def wlr(self) -> float:
        return utils.safe_div(self.wins, self.losses)

    @property
    def fkdr(self) -> float:
        return utils.safe_div(self.final_kills, self.final_deaths)

    @property
    def bblr(self) -> float:
        return utils.safe_div(self.beds_broken, self.beds_lost)

    def __post_init__(self):
        # type conversion
        for f in fields(self):
            value = getattr(self, f.name)
            if not value:
                continue
            if not isinstance(value, f.type):
                setattr(self, f.name, f.type(value))

@dataclass
class Bedwars:
    """Base model for bedwars stats.
    Attributes
    ----------
    """
    _data: dict = field(repr=False)
    level: int = 1 # default handling for this field is done in utils.py
    coins: int = 0
    kills: int = 0
    deaths: int = 0
    wins: int = 0
    losses: int = 0
    games_played: int = 0
    final_kills: int = 0
    final_deaths: int = 0
    beds_broken: int = 0
    beds_lost: int = 0
    winstreak: int = None # if None, winstreaks are disabled
    exp: int = 0
    # modes
    solo: BedwarsMode = field(init=False)
    doubles: BedwarsMode = field(init=False)
    threes: BedwarsMode = field(init=False)
    fours: BedwarsMode = field(init=False)
    teams: BedwarsMode = field(init=False)
    # other
    # island_topper: str = None
    # projectile_trail: str = None
    # death_cry: str = None
    # kill_effect: str = None
    # selected_ultimate: str = None

    @property
    def kdr(self) -> float:
        return utils.safe_div(self.kills, self.deaths)

    @property
    def wlr(self) -> float:
        return utils.safe_div(self.wins, self.losses)

    @property
    def fkdr(self) -> float:
        return utils.safe_div(self.final_kills, self.final_deaths)

    @property
    def bblr(self) -> float:
        return utils.safe_div(self.beds_broken, self.beds_lost)

    def __post_init__(self):
        # type conversion
        for f in fields(self):
            try:
                value = getattr(self, f.name)
            except AttributeError:
                continue
            if not value:
                continue
            elif not isinstance(value, f.type):
                setattr(self, f.name, f.type(value))

        modes = (
            'solo',
            'doubles',
            'threes',
            'fours',
            'teams',
        )
        for mode in modes:
            data = utils._clean(self._data, mode=f'BEDWARS_{mode.upper()}')
            setattr(self, mode, BedwarsMode(**data))
