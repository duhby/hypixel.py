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

from dataclasses import dataclass, field
from ... import utils

@dataclass
class DuelsMode:
    _data: dict = field(repr=False)
    _mode: str = field(repr=False)
    kills: int = 0
    deaths: int = 0
    wins: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    arrows_hit: int = 0
    arrows_shot: int = 0

    @property
    def wlr(self) -> float:
        return utils.safe_div(self.wins, self.losses)

    @property
    def mr(self) -> float:
        misses = self.melee_swings - self.melee_hits
        return utils.safe_div(self.melee_hits, misses)

    @property
    def ar(self) -> float:
        misses = self.arrows_shot - self.arrows_hit
        return utils.safe_div(self.arrows_hit, misses)

    @property
    def title(self) -> str:
        return utils.get_title(self._data, self._mode)

@dataclass
class Duels:
    _data: dict = field(repr=False)
    coins: int = 0
    kills: int = 0 # doesn't include bridge
    deaths: int = 0 # doesn't include bridge
    wins: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    arrows_hit: int = 0
    arrows_shot: int = 0
    blitz: DuelsMode = field(init=False)
    bow: DuelsMode = field(init=False)
    boxing: DuelsMode = field(init=False)
    bridge: DuelsMode = field(init=False)
    classic: DuelsMode = field(init=False)
    combo: DuelsMode = field(init=False)
    mega_walls: DuelsMode = field(init=False)
    no_debuff: DuelsMode = field(init=False)
    op: DuelsMode = field(init=False)
    parkour: DuelsMode = field(init=False)
    skywars: DuelsMode = field(init=False)
    sumo: DuelsMode = field(init=False)
    tnt_games: DuelsMode = field(init=False)
    uhc: DuelsMode = field(init=False)

    @property
    def wlr(self) -> float:
        return utils.safe_div(self.wins, self.losses)

    @property
    def mr(self) -> float:
        misses = self.melee_swings - self.melee_hits
        return utils.safe_div(self.melee_hits, misses)

    @property
    def ar(self) -> float:
        misses = self.arrows_shot - self.arrows_hit
        return utils.safe_div(self.arrows_hit, misses)

    @property
    def title(self) -> str:
        return utils.get_title(self._data, 'all_modes')

    def __post_init__(self):
        modes = (
            'blitz',
            'bow',
            'boxing',
            'bridge',
            'classic',
            'combo',
            'mega_walls',
            'no_debuff',
            'op',
            'parkour',
            'skywars',
            'sumo',
            'tnt_games',
            'uhc',
        )
        for mode in modes:
            data = utils._clean(self._data, mode=f'{mode.upper()}_DUELS')
            data['_data'] = self._data
            data['_mode'] = mode
            setattr(self, mode, DuelsMode(**data))
