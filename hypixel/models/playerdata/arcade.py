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
class CaptureTheWool:
    captures: int = 0
    kills_assists: int = 0
    # achievements: int = 0

@dataclass
class HypixelSays:
    rounds: int = 0
    wins: int = 0

    # math
    @property
    def losses(self) -> int:
        return rounds - wins

    @property
    def wlr(self) -> float:
        return utils.safe_div(self.wins, self.losses)

@dataclass
class PartyGames:
    wins: int = 0
    # legacy
    wins_2: int = 0
    wins_3: int = 0

    # math
    @property
    def total_wins(self) -> int:
        return self.wins + self.wins_2 + self.wins_3

@dataclass
class Arcade:
    _data: dict = field(repr=False)
    coins: int = 0

    def __post_init__(self):
        ctw_data = utils._clean(self._data, mode='CTW')
        self.ctw = CaptureTheWool(**ctw_data)

        hypixel_says_data = utils._clean(self._data, mode='HYPIXEL_SAYS')
        self.hypixel_says = HypixelSays(**hypixel_says_data)

        party_games_data = utils._clean(self._data, mode='PARTY_GAMES')
        self.party = PartyGames(**party_games_data)
