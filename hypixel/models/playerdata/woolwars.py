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
from ... import utils

from typing import Literal

__all__ = (
    'WoolWars',
    'WWClass',
)

WWClass = Literal['TANK', 'ASSULT', 'ARCHER', 'SWORDSMAN', 'GOLEM', 'ENGINEER']

@dataclass
class WoolWars:
    level: int = 1
    coins: int = 0
    kills: int = 0
    deaths: int = 0
    games: int = 0
    wins: int = 0
    losses: int = 0
    selected_class: WWClass = None

    def __post_init__(self):
        self.losses = self.games - self.wins
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.losses)
