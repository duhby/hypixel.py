"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'Blitz',
]


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
