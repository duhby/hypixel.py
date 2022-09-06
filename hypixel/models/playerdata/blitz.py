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
class Blitz:
    coins: int = 0
    kills: int = 0
    deaths: int = 0
    wins: int = 0
    wins_solo: int = 0
    wins_team: int = 0
    arrows_hit: int = 0
    arrows_shot: int = 0
    chests_opened: int = 0
    games: int = 0
    kdr: float = field(init=False)
    wlr: float = field(init=False)
    ar: float = field(init=False) # will be 0 if it doesn't have bows

    def __post_init__(self):
        self.coins = int(self.coins) # Normally float
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.deaths)
        self.ar = utils.safe_div(
            self.arrows_hit, self.arrows_shot - self.arrows_hit
        )
