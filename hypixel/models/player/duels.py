"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from . import utils

__all__ = [
    'Duels',
    'DuelsMode',
]


@dataclass
class DuelsMode:
    """Base model for duels gamemode stats.

    .. note::

        Some attributes may be 0 if a given gamemode doesn't use them.

    Attributes
    ----------
    kills: :class:`int`
        Kills.
    deaths: :class:`int`
        Deaths.
    wins: :class:`int`
        Wins.
    losses: :class:`int`
        Losses.
    melee_hits: :class:`int`
        Melee hits.
    melee_swings: :class:`int`
        Melee swings.
    arrows_hit: :class:`int`
        Arrows hit.
    arrows_shot: :class:`int`
        Arrows shot.
    wlr: :class:`float`
        Win loss ratio; self.wins / self.losses.
    mr: :class:`float`
        Melee ratio; self.melee_hits / self.melee_swings.
    ar: :class:`float`
        Arrow ratio; self.arrows_hit / self.arrows_shot.
    title: :class:`str`
        Duel title. This is the title that is displayed in the duels
        lobby. Defaults to ``Rookie I``.
    """
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
    wlr: float = field(init=False) # More accurate than kdr
    mr: float = field(init=False) # will be 0 if it doesn't have hits
    ar: float = field(init=False) # will be 0 if it doesn't have bows
    title: str = field(init=False)

    def __post_init__(self):
        self.wlr = utils.safe_div(self.wins, self.losses)
        self.mr = utils.safe_div(
            self.melee_hits, self.melee_swings - self.melee_hits
        )
        self.ar = utils.safe_div(
            self.arrows_hit, self.arrows_shot - self.arrows_hit
        )
        self.title = utils.get_title(self._data, self._mode)

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
    wlr: float = field(init=False)
    mr: float = field(init=False)
    ar: float = field(init=False)
    title: str = field(init=False)
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

    def __post_init__(self):
        self.wlr = utils.safe_div(self.wins, self.losses)
        self.mr = utils.safe_div(
            self.melee_hits, self.melee_swings - self.melee_hits
        )
        self.ar = utils.safe_div(
            self.arrows_hit, self.arrows_shot - self.arrows_hit
        )
        self.title = utils.get_title(self._data, 'all_modes')

        modes = [
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
        ]
        for mode in modes:
            data = utils._clean(self._data, mode=f'{mode.upper()}_DUELS')
            data['_data'] = self._data
            data['_mode'] = mode
            setattr(self, mode, DuelsMode(**data))
