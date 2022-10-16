"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field
from typing import Optional

from . import utils

__all__ = [
    'Bedwars',
    'BedwarsMode',
]


@dataclass
class BedwarsMode:
    """Base model for bedwars mode stats.

    Attributes
    ----------
    kills: :class:`int`
        Normal kills.
    deaths: :class:`int`
        Normal deaths.
    fall_deaths: :class:`int`
        Deaths from fall damage.
    void_deaths: :class:`int`
        Deaths from the void.
    wins: :class:`int`
        Wins.
    losses: :class:`int`
        Losses.
    games: :class:`int`
        Total games played.

        .. note::

            This number tends to be a bit higher than self.wins +
            self.losses for an unknown/unresearched reason.
    final_kills: :class:`int`
        Final kills.
    final_deaths: :class:`int`
        Final deaths.
    fall_final_deaths: :class:`int`
        Final deaths from fall damage.
    void_final_deaths: :class:`int`
        Final deaths from the void.
    beds_broken: :class:`int`
        Beds broken.
    beds_lost: :class:`int`
        Beds lost.
    kdr: :class:`float`
        Kill death ratio; self.kills / self.deaths.
    wlr: :class:`float`
        Win loss ratio; self.wins / self.losses.
    fkdr: :class:`float`
        Final kill death ratio; self.final_kills / self.final_deaths.
    bblr: :class:`float`
        Bed break bed loss ratio; self.beds_broken / self.beds_lost.
    """
    kills: int = 0
    deaths: int = 0
    fall_deaths: int = 0
    void_deaths: int = 0
    wins: int = 0
    losses: int = 0
    games: int = 0
    final_kills: int = 0
    final_deaths: int = 0
    fall_final_deaths: int = 0
    void_final_deaths: int = 0
    beds_broken: int = 0
    beds_lost: int = 0
    kdr: float = field(init=False)
    wlr: float = field(init=False)
    fkdr: float = field(init=False)
    bblr: float = field(init=False)

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.losses)
        self.fkdr = utils.safe_div(self.final_kills, self.final_deaths)
        self.bblr = utils.safe_div(self.beds_broken, self.beds_lost)

@dataclass
class Bedwars:
    """Base model for bedwars stats.

    .. note::

        Overall stats only include core modes.

    Attributes
    ----------
    level: :class:`int`
        Level.
    coins: :class:`int`
        Coins.
    kills: :class:`int`
        Normal kills.
    deaths: :class:`int`
        Normal deaths.
    fall_deaths: :class:`int`
        Deaths from fall damage.
    void_deaths: :class:`int`
        Deaths from the void.
    wins: :class:`int`
        Wins.
    losses: :class:`int`
        Losses.
    games: :class:`int`
        Total games played.

        .. note::

            This number is usually a bit higher than self.wins +
            self.losses for an unknown reason.
    final_kills: :class:`int`
        Final kills.
    final_deaths: :class:`int`
        Final deaths.
    fall_final_deaths: :class:`int`
        Final deaths from fall damage.
    void_final_deaths: :class:`int`
        Final deaths from the void.
    beds_broken: :class:`int`
        Beds broken.
    beds_lost: :class:`int`
        Beds lost.
    winstreak: Optional[:class:`int`]
        Winstreak.

        .. note::

            If the player has winstreaks disabled in their API settings,
            then this will be ``None``.
    exp: :class:`int`
        Experience points.
    kdr: :class:`float`
        Kill death ratio; self.kills / self.deaths.
    wlr: :class:`float`
        Win loss ratio; self.wins / self.losses.
    fkdr: :class:`float`
        Final kill death ratio; self.final_kills / self.final_deaths.
    bblr: :class:`float`
        Bed break bed loss ratio; self.beds_broken / self.beds_lost.
    solo: :class:`BedwarsMode`
        A model for abstracting solo bedwars data.
    doubles: :class:`BedwarsMode`
        A model for abstracting doubles bedwars data.
    threes: :class:`BedwarsMode`
        A model for abstracting threes bedwars data.
    fours: :class:`BedwarsMode`
        A model for abstracting fours bedwars data.
    teams: :class:`BedwarsMode`
        A model for abstracting teams bedwars data.
    """
    _data: dict = field(repr=False)
    level: int = 1 # Default handling in utils.h_utils._clean
    coins: int = 0
    kills: int = 0
    deaths: int = 0
    fall_deaths: int = 0
    void_deaths: int = 0
    wins: int = 0
    losses: int = 0
    games: int = 0
    final_kills: int = 0
    final_deaths: int = 0
    fall_final_deaths: int = 0
    void_final_deaths: int = 0
    beds_broken: int = 0
    beds_lost: int = 0
    winstreak: Optional[int] = None # winstreaks can be disabled
    exp: int = 0
    kdr: float = field(init=False)
    wlr: float = field(init=False)
    fkdr: float = field(init=False)
    bblr: float = field(init=False)
    solo: BedwarsMode = field(init=False)
    doubles: BedwarsMode = field(init=False)
    threes: BedwarsMode = field(init=False)
    fours: BedwarsMode = field(init=False)
    teams: BedwarsMode = field(init=False)
    # other
    # island_topper: str = None
    # projectile_trail: str = None
    # death_cry: str = None
    # kill_effect: str = None
    # selected_ultimate: str = None

    def __post_init__(self):
        self.kdr = utils.safe_div(self.kills, self.deaths)
        self.wlr = utils.safe_div(self.wins, self.losses)
        self.fkdr = utils.safe_div(self.final_kills, self.final_deaths)
        self.bblr = utils.safe_div(self.beds_broken, self.beds_lost)

        modes = [
            'solo',
            'doubles',
            'threes',
            'fours',
            'teams',
        ]
        for mode in modes:
            data = utils._clean(self._data, mode=f'BEDWARS_{mode.upper()}')
            setattr(self, mode, BedwarsMode(**data))
