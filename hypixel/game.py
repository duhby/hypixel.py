"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from __future__ import annotations
from dataclasses import dataclass
import functools

__all__ = [
    'Game',
]


@dataclass
class Game:
    """Represents a Hypixel game.

    Attributes
    ----------
    id: :class:`int`
        The id of the game.

        .. note::

            Although there are ids ranging from 2-68, there aren't 66
            game types as some are skipped for whatever reason.
    type_name: :class:`str`
        The type name used in Hypixel API attributes.
    database_name: :class:`str`
        The key value used in the Hypixel API.
    clean_name: :class:`str`
        The game name in Title Case
    standard_name: :class:`str`
        Sometimes shorter than ``self.clean_name``.
    legacy: :class:`bool`
        Whether or not the game is a legacy game.
    """
    id: int
    type_name: str
    database_name: str
    clean_name: str
    standard_name: str
    legacy: bool = False

    @classmethod
    @functools.lru_cache
    def from_type(cls, type_name: str) -> Game:
        """Constructs a :class:`Game` from its type name.

        Parameters
        ----------
        type_name: :class:`str`
            The type name used in Hypixel API attributes.
        """
        data = next((
            item for item in GAME_TYPES if item['type_name'] == type_name
        ), None)
        if not data:
            return None
        return cls(**data)

    @classmethod
    @functools.lru_cache
    def from_id(cls, id_: int) -> Game:
        """Constructs a :class:`Game` from its id.

        Parameters
        ----------
        id: :class:`int`
            The id number of the game.
        """
        data = next((
            item for item in GAME_TYPES if item['id'] == id_
        ), None)
        if not data:
            return None
        return cls(**data)

GAME_TYPES = [
  {
    'id': 2,
    'type_name': 'QUAKECRAFT',
    'database_name': 'Quake',
    'clean_name': 'Quake',
    'standard_name': 'Quake',
    'legacy': True,
  },
  {
    'id': 3,
    'type_name': 'WALLS',
    'database_name': 'Walls',
    'clean_name': 'Walls',
    'standard_name': 'Walls',
    'legacy': True,
  },
  {
    'id': 4,
    'type_name': 'PAINTBALL',
    'database_name': 'Paintball',
    'clean_name': 'Paintball',
    'standard_name': 'Paintball',
    'legacy': True,
  },
  {
    'id': 5,
    'type_name': 'SURVIVAL_GAMES',
    'database_name': 'HungerGames',
    'clean_name': 'Blitz Survival Games',
    'standard_name': 'Blitz',
  },
  {
    'id': 6,
    'type_name': 'TNTGAMES',
    'database_name': 'TNTGames',
    'clean_name': 'TNT Games',
    'standard_name': 'TNT',
  },
  {
    'id': 7,
    'type_name': 'VAMPIREZ',
    'database_name': 'VampireZ',
    'clean_name': 'VampireZ',
    'standard_name': 'VampireZ',
    'legacy': True,
  },
  {
    'id': 13,
    'type_name': 'WALLS3',
    'database_name': 'Walls3',
    'clean_name': 'Mega Walls',
    'standard_name': 'MegaWalls',
  },
  {
    'id': 14,
    'type_name': 'ARCADE',
    'database_name': 'Arcade',
    'clean_name': 'Arcade',
    'standard_name': 'Arcade',
  },
  {
    'id': 17,
    'type_name': 'ARENA',
    'database_name': 'Arena',
    'clean_name': 'Arena',
    'standard_name': 'Arena',
    'legacy': True,
  },
  {
    'id': 20,
    'type_name': 'UHC',
    'database_name': 'UHC',
    'clean_name': 'UHC Champions',
    'standard_name': 'UHC',
  },
  {
    'id': 21,
    'type_name': 'MCGO',
    'database_name': 'MCGO',
    'clean_name': 'Cops and Crims',
    'standard_name': 'CvC',
  },
  {
    'id': 23,
    'type_name': 'BATTLEGROUND',
    'database_name': 'Battleground',
    'clean_name': 'Warlords',
    'standard_name': 'Warlords',
  },
  {
    'id': 24,
    'type_name': 'SUPER_SMASH',
    'database_name': 'SuperSmash',
    'clean_name': 'Smash Heroes',
    'standard_name': 'Smash',
  },
  {
    'id': 25,
    'type_name': 'GINGERBREAD',
    'database_name': 'GingerBread',
    'clean_name': 'Turbo Kart Racers',
    'standard_name': 'TKR',
    'legacy': True,
  },
  {
    'id': 26,
    'type_name': 'HOUSING',
    'database_name': 'Housing',
    'clean_name': 'Housing',
    'standard_name': 'Housing',
  },
  {
    'id': 51,
    'type_name': 'SKYWARS',
    'database_name': 'SkyWars',
    'clean_name': 'SkyWars',
    'standard_name': 'SkyWars',
  },
  {
    'id': 52,
    'type_name': 'TRUE_COMBAT',
    'database_name': 'TrueCombat',
    'clean_name': 'Crazy Walls',
    'standard_name': 'CrazyWalls',
  },
  {
    'id': 54,
    'type_name': 'SPEED_UHC',
    'database_name': 'SpeedUHC',
    'clean_name': 'Speed UHC',
    'standard_name': 'SpeedUHC',
  },
  {
    'id': 55,
    'type_name': 'SKYCLASH',
    'database_name': 'SkyClash',
    'clean_name': 'SkyClash',
    'standard_name': 'SkyClash',
  },
  {
    'id': 56,
    'type_name': 'LEGACY',
    'database_name': 'Legacy',
    'clean_name': 'Classic Games',
    'standard_name': 'Classic',
    'legacy': True,
  },
  {
    'id': 57,
    'type_name': 'PROTOTYPE',
    'database_name': 'Prototype',
    'clean_name': 'Prototype',
    'standard_name': 'Prototype',
  },
  {
    'id': 58,
    'type_name': 'BEDWARS',
    'database_name': 'Bedwars',
    'clean_name': 'Bed Wars',
    'standard_name': 'Bed Wars',
  },
  {
    'id': 59,
    'type_name': 'MURDER_MYSTERY',
    'database_name': 'MurderMystery',
    'clean_name': 'Murder Mystery',
    'standard_name': 'MurderMystery',
  },
  {
    'id': 60,
    'type_name': 'BUILD_BATTLE',
    'database_name': 'BuildBattle',
    'clean_name': 'Build Battle',
    'standard_name': 'BuildBattle',
  },
  {
    'id': 61,
    'type_name': 'DUELS',
    'database_name': 'Duels',
    'clean_name': 'Duels',
    'standard_name': 'Duels',
  },
  {
    'id': 63,
    'type_name': 'SKYBLOCK',
    'database_name': 'SkyBlock',
    'clean_name': 'SkyBlock',
    'standard_name': 'SkyBlock',
  },
  {
    'id': 64,
    'type_name': 'PIT',
    'database_name': 'Pit',
    'clean_name': 'Pit',
    'standard_name': 'Pit',
  },
  {
    'id': 65,
    'type_name': 'REPLAY',
    'database_name': 'Replay',
    'clean_name': 'Replay',
    'standard_name': 'Replay',
  },
  {
    'id': 67,
    'type_name': 'SMP',
    'database_name': 'SMP',
    'clean_name': 'SMP',
    'standard_name': 'SMP',
  },
  {
    'id': 68,
    'type_name': 'WOOL_GAMES',
    'database_name': 'WoolGames',
    'clean_name': 'Wool Games',
    'standard_name': 'Wool Games',
  },
]
