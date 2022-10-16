"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field
from typing import Optional

from . import utils

__all__ = [
    'Skywars',
    'SkywarsMode',
]


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
    winstreak: Optional[int] = None # winstreaks can be disabled
    souls: int = 0
    exp: int = 0
    kdr: float = field(init=False)
    wlr: float = field(init=False)
    ar: float = field(init=False)
    ranked: SkywarsMode = field(init=False)
    solo_normal: SkywarsMode = field(init=False)
    solo_insane: SkywarsMode = field(init=False)
    team_normal: SkywarsMode = field(init=False)
    team_insane: SkywarsMode = field(init=False)
    mega_normal: SkywarsMode = field(init=False)
    mega_doubles: SkywarsMode = field(init=False)

    def __post_init__(self):
        self.level = utils.skywars_level(self.exp)
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.losses)
        self.ar = utils.safe_div(
            self.arrows_hit, self.arrows_shot - self.arrows_hit
        )

        modes = [
            'ranked',
            'solo_normal',
            'solo_insane',
            'team_normal',
            'team_insane',
            'mega_normal',
            'mega_doubles',
        ]
        for mode in modes:
            data = utils._clean(self._data, mode=f'SKYWARS_{mode.upper()}')
            setattr(self, mode, SkywarsMode(**data))
