"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'MurderMystery',
    'MurderMysteryMode',
]


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

        modes = [
            'assassins',
            'classic',
            'double_up',
            # 'infection',
            # Legacy :(
            'hardcore',
            'showdown',
        ]
        for mode in modes:
            data = utils._clean(self._data, mode=f'MM_{mode.upper()}')
            setattr(self, mode, MurderMysteryMode(**data))
