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

@dataclass
class HypixelSays:
    rounds: int = 0
    wins: int = 0
    losses: int = rounds - wins

    @property
    def wlr(self) -> float:
        return utils.safe_div(self.wins, self.losses)

@dataclass
class MiniWalls:
    kills: int = 0
    deaths: int = 0
    wins: int = 0
    final_kills: int = 0
    wither_kills: int = 0
    wither_damage: int = 0
    arrows_hit: int = 0
    arrows_shot: int = 0

    @property
    def kd(self) -> float:
        return utils.safe_div(self.kills, self.deaths)

@dataclass
class PartyGames:
    wins: int = 0
    # legacy
    wins_2: int = 0
    wins_3: int = 0

    @property
    def total_wins(self) -> int:
        return self.wins + self.wins_2 + self.wins_3

@dataclass
class Arcade:
    _data: dict = field(repr=False)
    coins: int = 0
    # gamemodes
    ctw: CaptureTheWool = field(init=False)
    hypixel_says: HypixelSays = field(init=False)
    mini_walls: MiniWalls = field(init=False)
    party_games: PartyGames = field(init=False)

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

        modes = {
            'ctw': CaptureTheWool,
            'hypixel_says': HypixelSays,
            'mini_walls': MiniWalls,
            'party_games': PartyGames,
        }
        for mode, model in modes.items():
            data = utils._clean(self._data, mode=mode.upper())
            setattr(self, mode, model(**data))
