"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'Uhc',
    'UhcMode',
]


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
    # solo_brawl: UhcMode = field(init=False)
    # duo_brawl: UhcMode = field(init=False)
    kdr: float = field(init=False)

    def __post_init__(self):
        self.level = utils.uhc_level(self.score)

        modes = (
            'solo',
            'team',
            'brawl',
            # 'solo_brawl',
            # 'duo_brawl',
        )
        for mode in modes:
            data = utils._clean(self._data, mode=f'UHC_{mode.upper()}')
            setattr(self, mode, UhcMode(**data))

        modes = [
            self.solo,
            self.team,
            self.brawl,
            # self.solo_brawl,
            # self.duo_brawl,
        ]
        self.wins = sum(mode.wins for mode in modes)
        self.kills = sum(mode.kills for mode in modes)
        self.deaths = sum(mode.deaths for mode in modes)
        self.heads_eaten = sum(mode.heads_eaten for mode in modes)
        self.ultimates_crafted = sum(mode.ultimates_crafted for mode in modes)
        self.kdr = utils.safe_div(self.kills, self.deaths)
