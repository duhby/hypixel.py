"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'Arcade',
    'CaptureTheWool',
    'HypixelSays',
    'MiniWalls',
    'PartyGames',
]


@dataclass
class CaptureTheWool:
    captures: int = 0
    kills_assists: int = 0

@dataclass
class HypixelSays:
    rounds: int = 0
    wins: int = 0
    top_score: int = 0
    losses: int = field(init=False)
    wlr: float = field(init=False)

    def __post_init__(self):
        self.losses = self.rounds - self.wins
        self.wlr = utils.safe_div(self.wins, self.losses)

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
    kdr: float = field(init=False)

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)

@dataclass
class PartyGames:
    wins: int = 0
    # legacy
    wins_2: int = 0
    wins_3: int = 0
    total_wins: int = field(init=False)

    def __post_init__(self):
        self.total_wins = self.wins + self.wins_2 + self.wins_3

@dataclass
class Arcade:
    _data: dict = field(repr=False)
    coins: int = 0
    ctw: CaptureTheWool = field(init=False)
    hypixel_says: HypixelSays = field(init=False)
    mini_walls: MiniWalls = field(init=False)
    party_games: PartyGames = field(init=False)

    def __post_init__(self):
        self.coins = int(self.coins) # Normally float
        modes = {
            'ctw': CaptureTheWool,
            'hypixel_says': HypixelSays,
            'mini_walls': MiniWalls,
            'party_games': PartyGames,
        }
        for mode, model in modes.items():
            data = utils._clean(self._data, mode=mode.upper())
            setattr(self, mode, model(**data))
