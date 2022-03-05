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

import functools
import asyncio
import time
from uuid import UUID

from .constants import aliases, get_game_type
from .errors import *

REQUIRE_COPY = getattr(aliases, 'REQUIRE_COPY')

def _clean(data: dict, mode: str, extra=None) -> dict:
    alias = getattr(aliases, mode)
    if mode in REQUIRE_COPY:
        _data = data.copy()

    if mode in ('ARCADE', 'HYPIXEL_SAYS', 'MINI_WALLS', 'PARTY_GAMES'):
        data = data.get('stats', {}).get('Arcade', {})

    elif mode == 'CTW':
        data = data.get('achievement_stats', {})

    elif mode == 'PLAYER':
        # avoid name conflicts
        data['achievement_stats'] = data.pop('achievements', {})

    elif mode == 'TKR':
        data = data.get('stats', {}).get('GingerBread', {})

    elif mode == 'BEDWARS':
        level = data.get('achievement_stats', {}).get('bedwars_level', 1)
        data = data.get('stats', {}).get('Bedwars', {})
        data['bedwars_level'] = level
        # copy here instead of before and after because BedwarsMode classes
        # need stats.Bedwars specific data
        data['_data'] = data.copy()

    elif mode == 'DUELS':
        data = data.get('stats', {}).get('Duels', {})

    elif mode == 'PAINTBALL':
        data = data.get('stats', {}).get('Paintball', {})

    elif mode == 'SOCIALS':
        data = data.get('socialMedia', {}).get('links', {})

    elif mode == 'FRIEND':
        # sender and receiver could be either the player or the friend
        # as the api stores the sender and receiver of the specific friend
        # request
        if data['uuidReceiver'] == extra:
            data['uuidReceiver'] = data['uuidSender']

    elif mode == 'STATUS':
        # convert game_type to GameType
        data['gameType'] = get_game_type(data.get('gameType'))

    if mode in REQUIRE_COPY:
        data['_data'] = _data

    # replace keys in data with their formatted alias
    replaced_data = {alias.get(k, k): v for k, v in data.items()}
    # remove unused/unsupported items
    return {key: replaced_data[key] for key in replaced_data if key in alias.values()}

def get_level(network_exp: int) -> float:
    return round(1 + (-8750.0 + (8750 ** 2 + 5000 * network_exp) ** 0.5) / 2500, 2)

def safe_div(a: int, b: int) -> float:
    if not b:
        return a
    else:
        return round(a / b, 2)

colors = ('§0', '§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8', '§9', '§a', '§b', '§c', '§d', '§e', '§f')
def clean_rank_prefix(string: str) -> str:
    for color in colors:
        string = string.replace(color, '')
    string = string.replace('[', '').replace(']', '')
    return string

# values past 10 aren't needed
# value = (100, 90, 50, 40, 10, 9, 5, 4, 1)
# symbol = ('C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
value = (10, 9, 5, 4, 1)
symbol = ('X', 'IX', 'V', 'IV', 'I')
def romanize(number: int) -> str:
    roman = ''
    i = 0
    while number > 0:
        for _ in range(number // value[i]):
            roman += symbol[i]
            number -= value[i]
        i += 1
    return roman

divisions = {
    'rookie': 'Rookie',
    'iron': 'Iron',
    'gold': 'Gold',
    'diamond': 'Diamond',
    'master': 'Master',
    'legend': 'Legend',
    'grandmaster': 'Grandmaster',
    'godlike': 'Godlike',
    'world_elite': 'WORLD ELITE',
    'world_master': 'WORLD MASTER',
    'worlds_best': 'WORLD\'S BEST',
}
def get_title(data: dict, mode: str) -> str:
    title = 'Rookie I'
    for key, value in divisions.items():
        prestige = data.get(f'{mode}_{key}_title_prestige')
        if prestige:
            # doesn't return instantly because
            # past division keys are still stored
            # return the last (current/highest) one
            title = f'{value} {romanize(prestige)}'
    return title

def async_timed_cache(function, max_age: int, max_size: int, typed=False):
    """Lru cache decorator with time-based cache invalidation and async
    implementation.
    """
    # _time_hash forces functools to provide TTL (time to live)
    @functools.lru_cache(maxsize=max_size, typed=typed)
    def _new_timed(*args, _time_hash, **kwargs):
        return asyncio.ensure_future(function(*args, **kwargs))

    @functools.lru_cache(maxsize=max_size, typed=typed)
    def _new(*args, **kwargs):
        return asyncio.ensure_future(function(*args, **kwargs))

    @functools.wraps(function)
    def _wrapped(*args, **kwargs):
        if max_age <= 0:
            return _new(*args, **kwargs)
        salt = int(time.monotonic() / max_age)
        return _new_timed(*args, **kwargs, _time_hash=salt)

    if max_age <= 0:
        _wrapped.cache_info = _new.cache_info
        _wrapped.clear_cache = _new.cache_clear
    else:
        _wrapped.cache_info = _new_timed.cache_info
        _wrapped.clear_cache = _new_timed.cache_clear

    return _wrapped

class HashedDict(dict):
    def __hash__(self):
        fs = frozenset(self.items())
        return hash(fs)

# only works on asynchronous instance methods where the first non-self
# parameter is the id
def convert_id(function):
    @functools.wraps(function)
    async def _wrapped(obj, id_, *args, **kwargs):
        if not isinstance(id_, str):
            raise InvalidPlayerId(id_)
        try:
            UUID(id_)
        except ValueError:
            uuid = await obj._get_uuid(name=id_)
        else:
            uuid = id_

        id_ = {'uuid': uuid, 'orig': id_}
        
        return await function(obj, id_, *args, **kwargs)
        
    return _wrapped
