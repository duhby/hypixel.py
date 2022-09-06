"""
The MIT License

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
import random
import math
from uuid import UUID
from typing import Optional
from datetime import datetime, timezone, timedelta
from string import Formatter

from .models import GameType, ColorType, GuildRank
from .constants.aliases import *
from .constants import GAME_TYPES, COLOR_TYPES
from .errors import *


# @functools.lru_cache
# def get_game(database_name) -> Optional[GameType]:
#     data = next((
#         item for item in GAME_TYPES if item['database_name'] == database_name
#     ), None)
#     if not data:
#         return None
#     return GameType(**data)


@functools.lru_cache
def get_game_type(type_name) -> Optional[GameType]:
    data = next((
        item for item in GAME_TYPES if item['type_name'] == type_name
    ), None)
    if not data:
        return None
    return GameType(**data)


REQUIRE_COPY = (
    'ARCADE',
    'HYPIXEL_SAYS',
    'MINI_WALLS',
    'PARTY_GAMES',
)
def _clean(data: dict, mode: str, extra=None) -> dict:
    alias = globals()[mode]
    if mode in REQUIRE_COPY:
        _data = data.copy()

    if mode in ('ARCADE', 'HYPIXEL_SAYS', 'MINI_WALLS', 'PARTY_GAMES'):
        data = data.get('stats', {}).get('Arcade', {})

    elif mode == 'CTW':
        data = data.get('achievement_stats', {})

    elif mode == 'PLAYER':
        # avoid name conflicts
        data['achievement_stats'] = data.pop('achievements', {})

    elif mode == 'PARKOUR':
        # return here because _data is needed after aliases are converted
        data = data.get('parkourCompletions', {})
        replaced_data = {alias.get(k, k): v for k, v in data.items()}
        data = {
            key: replaced_data[key]
            for key in replaced_data if key in alias.values()
        }
        return {'_data': data}

    elif mode == 'TKR':
        data = data.get('stats', {}).get('GingerBread', {})

    elif mode == 'MURDER_MYSTERY':
        data = data.get('stats', {}).get('MurderMystery', {})
        data['_data'] = data.copy()

    elif mode == 'UHC':
        data = data.get('stats', {}).get('UHC', {})
        data['_data'] = data.copy()

    elif mode in ('MM_HARDCORE', 'MM_SHOWDOWN'):
        data['removed'] = True

    elif mode == 'BEDWARS':
        level = data.get('achievement_stats', {}).get('bedwars_level', 1)
        data = data.get('stats', {}).get('Bedwars', {})
        data['bedwars_level'] = level
        # Copy here instead of before and after because BedwarsMode classes
        # need stats.Bedwars specific data.
        data['_data'] = data.copy()

    elif mode == 'SKYWARS':
        data = data.get('stats', {}).get('SkyWars', {})
        # Copy here instead of before and after because SkywarsMode classes
        # need stats.SkyWars specific data.
        data['_data'] = data.copy()

    elif mode == 'DUELS':
        data = data.get('stats', {}).get('Duels', {})
        # copy here instead of before and after because DuelsMode classes
        # need stats.Duels specific data
        data['_data'] = data.copy()

    elif mode == 'PAINTBALL':
        data = data.get('stats', {}).get('Paintball', {})

    elif mode == 'SOCIALS':
        data = data.get('socialMedia', {}).get('links', {})

    elif mode == 'FRIEND':
        # Sender and receiver could be either the player or the friend
        # as the api stores the sender and receiver of the specific friend
        # request.
        # Extra is the player's uuid.
        if data['uuidReceiver'] == extra:
            data['uuidReceiver'] = data['uuidSender']

    elif mode == 'STATUS':
        # convert game_type to GameType
        data['gameType'] = get_game_type(data.get('gameType'))

    elif mode == 'GUILD':
        achievements = data.get('achievements', {})
        data['winners'] = achievements.get('WINNERS')
        data['experience_kings'] = achievements.get('EXPERIENCE_KINGS')
        data['most_online_players'] = achievements.get('ONLINE_PLAYERS')

    elif mode == 'GUILD_MEMBER':
        # Extra is the guild's ranks.
        rank = next((
            rank for rank in extra if rank.name == data['rank']
        ), None)
        if rank is not None:
            data['rank'] = extra
        else:
            # TODO: get a list of legacy ranks like Guild Master and Officer
            data['rank'] = GuildRank(name=data['rank'])

    elif mode == 'BLITZ':
        data = data.get('stats', {}).get('HungerGames', {})

    if mode in REQUIRE_COPY:
        data['_data'] = _data

    # Replace keys in data with formatted alias
    # Remove items that are not in the alias dictionary
    return {alias.get(k, k): v for k, v in data.items() if k in alias.keys()}
    # replace keys in data with their formatted alias
    # return replaced_data = {alias.get(k, k): v for k, v in data.items()}
    # remove unused/unsupported items
    # return {key: replaced_data[key] for key in replaced_data if key in alias.values()}


def get_level(network_exp: int) -> float:
    return round(1 + (-8750.0 + (8750 ** 2 + 5000 * network_exp) ** 0.5) / 2500, 2)


def safe_div(a: int, b: int) -> float:
    if not b:
        return float(a)
    else:
        return round(a / b, 2)


colors = ('§0', '§1', '§2', '§3', '§4', '§5', '§6', '§7',
          '§8', '§9', '§a', '§b', '§c', '§d', '§e', '§f')
def clean_rank_prefix(string: str) -> str:
    # .replace is faster than re.sub
    for color in colors:
        string = string.replace(color, '')
    string = string.replace('[', '').replace(']', '')
    return string

def wool_wars_level(exp: int) -> float:
    pass

# Values past 10 aren't needed, but still works up to 40.
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
            # Doesn't return instantly because
            # past division keys are still stored.
            # Return the last (current/highest) one.
            title = f'{value} {romanize(prestige)}'
    return title


def async_timed_cache(function, max_age: int, max_size: int, typed=False):
    """Lru cache decorator with time-based cache invalidation and async
    implementation.
    """
    # _time_hash forces functools to provide a time to live.
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


# For asynchronous instance methods whose first non-self
# parameter is a player id (string of uuid or username).
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


def get_rank(raw):
    """Return the rank of the player."""
    display_rank = None
    player = raw.get('player', {})
    pr = player.get('packageRank')
    npr = player.get('newPackageRank')
    mpr = player.get('monthlyPackageRank')
    prefix = player.get('prefix')
    rank = player.get('rank')
    if prefix:
        return clean_rank_prefix(prefix)
    elif rank:
        if rank == 'YOUTUBER':
            return 'YOUTUBE'
        # Old accounts with the 'rank' attribute that aren't
        # youtubers can also have a 'packageRank' attribute
        # instead of the newer ones.
        elif pr:
            return pr.replace('_', '').replace('PLUS', '+')
        # Some old accounts have this lol (ex. notch)
        elif rank == 'NORMAL':
            return None
        return rank.replace('_', ' ')
    elif mpr == 'SUPERSTAR':
        return 'MVP++'
    elif npr and npr != 'NONE':
        display_rank = npr
    else:
        return None
    return display_rank.replace('_', '').replace('PLUS', '+')


@functools.lru_cache
def get_color_type(type_name) -> Optional[ColorType]:
    data = next((
        item for item in COLOR_TYPES if item['type_name'] == type_name
    ), None)
    if not data:
        return None
    return ColorType(**data)


def _add_tzinfo(dt, tzinfo=timezone.utc) -> datetime:
    return dt.replace(tzinfo=tzinfo)


def convert_to_datetime(decimal, add_tzinfo=True) -> datetime:
    # Float division is cheaper than integer division.
    # Precision is a non-issue as decimals go only to the thousandth place.
    seconds = decimal / 1e3
    dt = datetime.fromtimestamp(seconds)
    if add_tzinfo:
        return _add_tzinfo(dt)
    return dt


# By MarredCheese and tomatoeshift on StackOverflow
def strfdelta(tdelta, fmt='{M:02}:{S:02.0f}.{mS}', inputtype='timedelta'):
    """Convert a datetime.timedelta object or a regular number to a custom-
    formatted string, just like the stftime() method does for datetime.datetime
    objects.

    The fmt argument allows custom formatting to be specified.  Fields can 
    include seconds, minutes, hours, days, and weeks.  Each field is optional.

    Some examples:
        '{D:02}d {H:02}h {M:02}m {S:02.0f}s' --> '05d 08h 04m 02s' (default)
        '{W}w {D}d {H}:{M:02}:{S:02.0f}'     --> '4w 5d 8:04:02'
        '{D:2}d {H:2}:{M:02}:{S:02.0f}'      --> ' 5d  8:04:02'
        '{H}h {S:.0f}s'                       --> '72h 800s'

    The inputtype argument allows tdelta to be a regular number instead of the  
    default, which is a datetime.timedelta object.  Valid inputtype strings: 
        's', 'seconds', 
        'm', 'minutes', 
        'h', 'hours', 
        'd', 'days', 
        'w', 'weeks'
    """

    # Convert tdelta to integer seconds.
    if inputtype == 'timedelta':
        remainder = tdelta.total_seconds()
    elif inputtype in ['s', 'seconds']:
        remainder = float(tdelta)
    elif inputtype in ['m', 'minutes']:
        remainder = float(tdelta)*60
    elif inputtype in ['h', 'hours']:
        remainder = float(tdelta)*3600
    elif inputtype in ['d', 'days']:
        remainder = float(tdelta)*86400
    elif inputtype in ['w', 'weeks']:
        remainder = float(tdelta)*604800

    f = Formatter()
    desired_fields = [field_tuple[1] for field_tuple in f.parse(fmt)]
    possible_fields = ('Y','m','W', 'D', 'H', 'M', 'S', 'mS', 'µS')
    constants = {'Y':86400*365.24,'m': 86400*30.44 ,'W': 604800, 'D': 86400, 'H': 3600, 'M': 60, 'S': 1, 'mS': 1/pow(10,3) , 'µS':1/pow(10,6)}
    values = {}
    for field in possible_fields:
        if field in desired_fields and field in constants:
            Quotient, remainder = divmod(remainder, constants[field])
            values[field] = int(Quotient) if field != 'S' else Quotient + remainder
    return f.format(fmt, **values)


"""
MIT License

Copyright (c) 2018 The Slothpixel Project
"""

# Length 12
xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
def skywars_level(exp) -> float:
    if exp >= 15000:
        return (exp - 15000) / 10000 + 12
    for i in range(12):
        if exp < xps[i]:
            return i + (exp - xps[i - 1]) / (xps[i] - xps[i - 1])


# Length 15
EXP_NEEDED = (
    100000,
    150000,
    250000,
    500000,
    750000,
    1000000,
    1250000,
    1500000,
    2000000,
    2500000,
    2500000,
    2500000,
    2500000,
    2500000,
    3000000,
)
MAX_LEVEL = 1000
def guild_level(exp: int) -> float:
    level = 0
    for i in range(MAX_LEVEL + 1):
        # required exp to get to the next level
        need = 0
        if i >= 15:
            need = EXP_NEEDED[-1]
        else:
            need = EXP_NEEDED[i]

        # return the current level plus progress towards the next (unused)
        # if the required exp is met, otherwise increment the level and
        # subtract the used exp
        if exp - need < 0:
            return round((level + (exp / need)) * 100) / 100
        level += 1
        exp -= need
    return MAX_LEVEL


xps = [0, 10, 60, 210, 460, 960, 1710, 2710, 5210, 10210, 13210, 16210,
       19210, 22210, 25210]
def uhc_level(exp):
    level = 0
    for xp in xps:
        if exp >= xp:
            level += 1
        else:
            break
    return level


"""
The MIT License

Copyright (c) 2015-present Rapptz
"""

class ExponentialBackoff:
    """An implementation of the exponential backoff algorithm

    Provides a convenient interface to implement an exponential backoff
    for reconnecting or retrying transmissions in a distributed network.

    Once instantiated, the delay method will return the next interval to
    wait for when retrying a connection or transmission.  The maximum
    delay increases exponentially with each retry up to a maximum of
    2^10 * base, and is reset if no more attempts are needed in a period
    of 2^11 * base seconds.

    .
        Raises
        ------
        timeout error thing
    """

    def __init__(self, timeout: int = 2**11):
        self._base: int = 2
        self._exp: int = 0
        self._max: int = 10
        self._timeout: int = timeout
        self._last_invocation: float = time.monotonic()

        # Use our own random instance to avoid messing with global one.
        rand = random.Random()
        rand.seed()

        # self._randfunc = rand.randrange
        self._randfunc = rand.uniform

    def delay(self) -> float:
        """Compute the next delay

        Returns the next delay to wait according to the exponential
        backoff algorithm.  This is a value between 0 and base * 2^exp
        where exponent starts off at 1 and is incremented at every
        invocation of this method up to a maximum of 10.

        If a period of more than base * 2^11 has passed since the last
        retry, the exponent is reset to 1.
        """
        invocation = time.monotonic()
        interval = invocation - self._last_invocation
        self._last_invocation = invocation
        
        if interval > self._timeout:
            raise TimeoutError('mojang')
            # self._exp = 0

        self._exp = min(self._exp + 1, self._max)
        return self._randfunc(0, self._base * 2**self._exp)
