"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'Paintball',
]


@dataclass
class Paintball:
    coins: int = 0
    wins: int = 0
    kills: int = 0
    deaths: int = 0
    killstreaks: int = 0
    shots_fired: int = 0
    kdr: float = field(init=False)
    skr: float = field(init=False)

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.skr = utils.safe_div(self.shots_fired, self.kills)
