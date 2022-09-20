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

from dataclasses import dataclass, field
from ... import utils

__all__ = (
    'Uhc',
    'UhcMode',
)

@dataclass
class UhcMode:
    wins: int = 0
    kills: int = 0
    deaths: int = 0
    heads_eaten: int = 0
    ultimates_crafted: int = 0
    kdr: float = field(init=False)

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)

@dataclass
class Uhc:
    _data: dict = field(repr=False)
    level: int = field(init=False)
    coins: int = 0
    score: int = 0
    parkour_1: bool = False
    parkour_2: bool = False
    wins: int = field(init=False)
    kills: int = field(init=False)
    deaths: int = field(init=False)
    heads_eaten: int = field(init=False)
    ultimates_crafted: int = field(init=False)
    solo: UhcMode = field(init=False)
    team: UhcMode = field(init=False)
    brawl: UhcMode = field(init=False)
    solo_brawl: UhcMode = field(init=False)
    duo_brawl: UhcMode = field(init=False)
    kdr: float = field(init=False)

    def __post_init__(self):
        self.level = utils.uhc_level(self.score)

        modes = (
            'solo',
            'team',
            'brawl',
            'solo_brawl',
            'duo_brawl',
        )
        for mode in modes:
            data = utils._clean(self._data, mode=f'UHC_{mode.upper()}')
            setattr(self, mode, UhcMode(**data))

        modes = [
            self.solo,
            self.team,
            self.brawl,
            self.solo_brawl,
            self.duo_brawl,
        ]
        self.wins = sum(mode.wins for mode in modes)
        self.kills = sum(mode.kills for mode in modes)
        self.deaths = sum(mode.deaths for mode in modes)
        self.heads_eaten = sum(mode.heads_eaten for mode in modes)
        self.ultimates_crafted = sum(mode.ultimates_crafted for mode in modes)
        self.kdr = utils.safe_div(self.kills, self.deaths)
