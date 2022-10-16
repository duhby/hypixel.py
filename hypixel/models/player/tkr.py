"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'TurboKartRacers',
]


@dataclass
class TurboKartRacers:
    coins: int = 0
    laps: int = 0
    gold: int = 0
    silver: int = 0
    bronze: int = 0
    blue_torpedo_hits: int = 0
    banana_hits: int = 0
    bananas_received: int = 0
    wins: int = 0 # top 3
    br: float = field(init=False)

    def __post_init__(self):
        self.br = utils.safe_div(self.banana_hits, self.bananas_received)
