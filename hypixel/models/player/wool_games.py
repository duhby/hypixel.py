"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'WoolGames',
    'WoolGamesMode',
]


@dataclass
class WoolGamesMode:
    kills: int = 0
    deaths: int = 0
    assists: int = 0
    wins: int = 0
    losses: int = field(init=False)
    games: int = 0
    blocks_broken: int = 0
    wool_placed: int = 0
    # 'TANK', 'ASSULT', 'ARCHER', 'SWORDSMAN', 'GOLEM', 'ENGINEER'
    selected_class: str = None
    kdr: float = field(init=False)
    wlr: float = field(init=False)

    def __post_init__(self):
        self.losses = self.games - self.wins
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.losses)

@dataclass
class WoolGames:
    _data: dict = field(repr=False)
    level: int = 1 # Default handling in utils._clean
    coins: int = 0
    exp: int = 0 # Rounded from float because precision is redundant
    wool_wars: WoolGamesMode = field(init=False)

    def __post_init__(self):
        self.level = utils.get_wool_wars_level(self.exp)

        # Future proofing I guess (API is structured this way)
        modes = [
            'wool_wars',
        ]
        for mode in modes:
            data = utils._clean(self._data, mode=f'WOOL_GAMES_{mode.upper()}')
            setattr(self, mode, WoolGamesMode(**data))
