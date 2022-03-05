"""
The MIT License (MIT)

Copyright (c) 2021-present duhby

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations
from typing import Optional
import functools
import hypixel # can't import GameType directly; circular imports :(
from .. import utils

__all__ = (
    'get_game',
    'get_game_type',
    'GAME_TYPES',
)

# from database name
@functools.lru_cache
def get_game(database_name) -> Optional[GameType]:
    data = next((
        item for item in GAME_TYPES if item['database_name'] == database_name
    ), None)
    if not data:
        return None
    return hypixel.models.GameType(**data)

# from type name (from gameType in /status)
def get_game_type(type_name) -> Optional[GameType]:
    data = next((
        item for item in GAME_TYPES if item['type_name'] == type_name
    ), None)
    if not data:
        return None
    return hypixel.models.GameType(**data)

# ---------------------------------------------------------------------- #

"""
The MIT License (MIT)

Copyright (c) 2017 The OpenDota Project, The Slothpixel Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

GAME_TYPES = [
  {
    'id': 2,
    'type_name': 'QUAKECRAFT',
    'database_name': 'Quake',
    'clean_name': 'Quake',
    'standard_name': 'Quake',
    'legacy': True
  },
  {
    'id': 3,
    'type_name': 'WALLS',
    'database_name': 'Walls',
    'clean_name': 'Walls',
    'standard_name': 'Walls',
    'legacy': True
  },
  {
    'id': 4,
    'type_name': 'PAINTBALL',
    'database_name': 'Paintball',
    'clean_name': 'Paintball',
    'standard_name': 'Paintball',
    'legacy': True
  },
  {
    'id': 5,
    'type_name': 'SURVIVAL_GAMES',
    'database_name': 'HungerGames',
    'lobby_name': 'blitz',
    'clean_name': 'Blitz Survival Games',
    'standard_name': 'Blitz'
  },
  {
    'id': 6,
    'type_name': 'TNTGAMES',
    'database_name': 'TNTGames',
    'lobby_name': 'tnt',
    'clean_name': 'TNT Games',
    'standard_name': 'TNT'
  },
  {
    'id': 7,
    'type_name': 'VAMPIREZ',
    'database_name': 'VampireZ',
    'clean_name': 'VampireZ',
    'standard_name': 'VampireZ',
    'legacy': True
  },
  {
    'id': 13,
    'type_name': 'WALLS3',
    'database_name': 'Walls3',
    'lobby_name': 'megawalls',
    'clean_name': 'Mega Walls',
    'standard_name': 'MegaWalls'
  },
  {
    'id': 14,
    'type_name': 'ARCADE',
    'database_name': 'Arcade',
    'lobby_name': 'arcade',
    'clean_name': 'Arcade',
    'standard_name': 'Arcade'
  },
  {
    'id': 17,
    'type_name': 'ARENA',
    'database_name': 'Arena',
    'clean_name': 'Arena',
    'standard_name': 'Arena',
    'legacy': True
  },
  {
    'id': 20,
    'type_name': 'UHC',
    'database_name': 'UHC',
    'lobby_name': 'uhc',
    'clean_name': 'UHC Champions',
    'standard_name': 'UHC'
  },
  {
    'id': 21,
    'type_name': 'MCGO',
    'database_name': 'MCGO',
    'lobby_name': 'mcgo',
    'clean_name': 'Cops and Crims',
    'standard_name': 'CvC'
  },
  {
    'id': 23,
    'type_name': 'BATTLEGROUND',
    'database_name': 'Battleground',
    'lobby_name': 'bg',
    'clean_name': 'Warlords',
    'standard_name': 'Warlords'
  },
  {
    'id': 24,
    'type_name': 'SUPER_SMASH',
    'database_name': 'SuperSmash',
    'lobby_name': 'smash',
    'clean_name': 'Smash Heroes',
    'standard_name': 'Smash'
  },
  {
    'id': 25,
    'type_name': 'GINGERBREAD',
    'database_name': 'GingerBread',
    'clean_name': 'Turbo Kart Racers',
    'standard_name': 'TKR',
    'legacy': True
  },
  {
    'id': 26,
    'type_name': 'HOUSING',
    'database_name': 'Housing',
    'clean_name': 'Housing',
    'standard_name': 'Housing'
  },
  {
    'id': 51,
    'type_name': 'SKYWARS',
    'database_name': 'SkyWars',
    'lobby_name': 'sw',
    'clean_name': 'SkyWars',
    'standard_name': 'SkyWars'
  },
  {
    'id': 52,
    'type_name': 'TRUE_COMBAT',
    'database_name': 'TrueCombat',
    'lobby_name': 'Truepvp',
    'clean_name': 'Crazy Walls',
    'standard_name': 'CrazyWalls'
  },
  {
    'id': 54,
    'type_name': 'SPEED_UHC',
    'database_name': 'SpeedUHC',
    'lobby_name': 'speeduhc',
    'clean_name': 'Speed UHC',
    'standard_name': 'SpeedUHC'
  },
  {
    'id': 55,
    'type_name': 'SKYCLASH',
    'database_name': 'SkyClash',
    'lobby_name': 'skyclash',
    'clean_name': 'SkyClash',
    'standard_name': 'SkyClash'
  },
  {
    'id': 56,
    'type_name': 'LEGACY',
    'database_name': 'Legacy',
    'lobby_name': 'legacy',
    'clean_name': 'Classic Games',
    'standard_name': 'Classic',
    'legacy': True
  },
  {
    'id': 57,
    'type_name': 'PROTOTYPE',
    'database_name': 'Prototype',
    'lobby_name': 'prototype',
    'clean_name': 'Prototype',
    'standard_name': 'Prototype'
  },
  {
    'id': 58,
    'type_name': 'BEDWARS',
    'database_name': 'Bedwars',
    'lobby_name': 'bedwars',
    'clean_name': 'Bed Wars',
    'standard_name': 'BedWars'
  },
  {
    'id': 59,
    'type_name': 'MURDER_MYSTERY',
    'database_name': 'MurderMystery',
    'lobby_name': 'mm',
    'clean_name': 'Murder Mystery',
    'standard_name': 'MurderMystery'
  },
  {
    'id': 60,
    'type_name': 'BUILD_BATTLE',
    'database_name': 'BuildBattle',
    'lobby_name': 'bb',
    'clean_name': 'Build Battle',
    'standard_name': 'BuildBattle'
  },
  {
    'id': 61,
    'type_name': 'DUELS',
    'database_name': 'Duels',
    'lobby_name': 'duels',
    'clean_name': 'Duels',
    'standard_name': 'Duels'
  },
  {
    'id': 63,
    'type_name': 'SKYBLOCK',
    'database_name': 'SkyBlock',
    'clean_name': 'SkyBlock',
    'standard_name': 'SkyBlock'
  },
  {
    'id': 64,
    'type_name': 'PIT',
    'database_name': 'Pit',
    'clean_name': 'Pit',
    'standard_name': 'Pit'
  },
  {
    'id': 65,
    'type_name': 'REPLAY',
    'database_name': 'Replay',
    'clean_name': 'Replay',
    'standard_name': 'Replay'
  },
  {
    'id': 67,
    'type_name': 'SMP',
    'database_name': 'SMP',
    'clean_name': 'SMP',
    'standard_name': 'SMP'
  }
]
