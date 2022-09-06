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

@dataclass
class SkywarsMode:
    kills: int = 0
    deaths: int = 0
    wins: int = 0
    losses: int = 0
    kdr: float = field(init=False)
    wlr: float = field(init=False)

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.losses)

@dataclass
class Skywars:
    _data: dict = field(repr=False)
    level: float = field(init=False)
    coins: int = 0
    kills: int = 0
    deaths: int = 0
    wins: int = 0
    losses: int = 0
    games: int = 0
    arrows_hit: int = 0
    arrows_shot: int = 0
    winstreak: int = None # winstreaks can be disabled # win_streak
    souls: int = 0
    exp: int = 0
    kdr: float = field(init=False)
    wlr: float = field(init=False)
    ar: float = field(init=False)
    solo_normal: SkywarsMode = field(init=False)
    solo_insane: SkywarsMode = field(init=False)
    team_normal: SkywarsMode = field(init=False)
    team_insane: SkywarsMode = field(init=False)
    ranked: SkywarsMode = field(init=False)
    mega: SkywarsMode = field(init=False)

    def __post_init__(self):
        self.level = utils.skywars_level(self.exp)
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.losses)
        self.ar = utils.safe_div(
            self.arrows_hit, self.arrows_shot - self.arrows_hit
        )

        modes = (
            'ranked',
            'solo_normal',
            'solo_insane',
            'team_normal',
            'team_insane',
            'mega_normal',
            'mega_doubles',
        )
        for mode in modes:
            data = utils._clean(self._data, mode=f'SKYWARS_{mode.upper()}')
            setattr(self, mode, SkywarsMode(**data))
