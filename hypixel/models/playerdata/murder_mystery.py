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
class MurderMysteryMode:
    games: int = 0
    wins: int = 0
    kills: int = 0
    deaths: int = 0
    bow_kills: int = 0
    knife_kills: int = 0
    thrown_knife_kills: int = 0
    removed: bool = False
    kdr: float = field(init=False)

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)

@dataclass
class MurderMystery:
    _data: dict = field(repr=False)
    coins: int = 0
    games: int = 0
    wins: int = 0
    kills: int = 0
    deaths: int = 0
    bow_kills: int = 0
    knife_kills: int = 0
    thrown_knife_kills: int = 0
    murderer_wins: int = 0
    detective_wins: int = 0
    # fastest_murderer_win: timedelta = None
    # fastest_detective_win: timedelta = None
    kdr: float = field(init=False)
    assassins: MurderMysteryMode = field(init=False)
    classic: MurderMysteryMode = field(init=False)
    double_up: MurderMysteryMode = field(init=False)
    hardcore: MurderMysteryMode = field(init=False)
    showdown: MurderMysteryMode = field(init=False)

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)

        modes = (
            'assassins',
            'classic',
            'double_up',
            # 'infection',
            # Removed :(
            'hardcore',
            'showdown',
        )
        for mode in modes:
            data = utils._clean(self._data, mode=f'MM_{mode.upper()}')
            setattr(self, mode, MurderMysteryMode(**data))
