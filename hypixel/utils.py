"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

import asyncio
import functools
import random
from string import Formatter
import time
from uuid import UUID

from .aliases import *
from .errors import InvalidPlayerId, TimeoutError
from .game import Game


def _clean(data: dict, mode: str, extra=None) -> dict:
    alias = globals()[mode]

    if mode == 'PLAYER':
        # avoid name conflicts
        data['achievement_stats'] = data.pop('achievements', {})

    elif mode == 'FRIEND':
        # Sender and receiver could be either the player or the friend
        # as the api stores the sender and receiver of the actual friend
        # request.
        # Extra is the player's uuid.
        if data['uuidReceiver'] == extra:
            data['uuidReceiver'] = data['uuidSender']

    elif mode == 'STATUS':
        data['gameType'] = Game.from_type(data.get('gameType'))

    elif mode == 'GUILD':
        achievements = data.get('achievements', {})
        data['winners'] = achievements.get('WINNERS')
        data['experience_kings'] = achievements.get('EXPERIENCE_KINGS')
        data['most_online_players'] = achievements.get('ONLINE_PLAYERS')

    # Replace keys in data with formatted alias
    # Remove items that are not in the alias dictionary
    return {alias.get(k, k): v for k, v in data.items() if k in alias.keys()}

def async_timed_cache(function, max_age: int, max_size: int, typed=False):
    """Lru cache decorator with time-based cache invalidation and async
    implementation."""
    # _time_hash forces functools to provide a ttl.
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

# For asynchronous instance methods whose first non-self parameter is a
# player id (string of uuid or username).
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

# By MarredCheese and tomatoeshift on StackOverflow
def strfdelta(tdelta, fmt='{M:02}:{S:02.0f}.{mS}', inputtype='timedelta'):
    """Convert a datetime.timedelta object or a regular number to a
    custom-formatted string, just like the stftime() method does for
    datetime.datetime objects.

    The fmt argument allows custom formatting to be specified. Fields
    can include seconds, minutes, hours, days, and weeks. Each field is
    optional.

    Some examples (first being the default):
        '{D:02}d {H:02}h {M:02}m {S:02.0f}s' --> '05d 08h 04m 02s'
        '{W}w {D}d {H}:{M:02}:{S:02.0f}'     --> '4w 5d 8:04:02'
        '{D:2}d {H:2}:{M:02}:{S:02.0f}'      --> ' 5d  8:04:02'
        '{H}h {S:.0f}s'                      --> '72h 800s'

    The inputtype argument allows tdelta to be a regular number instead
    of the default, which is a datetime.timedelta object. Valid
    inputtype strings:
        's', 'seconds',
        'm', 'minutes',
        'h', 'hours',
        'd', 'days',
        'w', 'weeks',
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
    constants = {
        'Y': 86400*365.24,
        'm': 86400*30.44,
        'W': 604800,
        'D': 86400,
        'H': 3600,
        'M': 60,
        'S': 1,
        'mS': 1/pow(10,3),
        'µS': 1/pow(10,6),
    }
    values = {}
    for field in possible_fields:
        if field in desired_fields and field in constants:
            Quotient, remainder = divmod(remainder, constants[field])
            values[field] = int(Quotient) if field != 'S' else Quotient + remainder
    return f.format(fmt, **values)


"""
The MIT License

Copyright (c) 2015-present Rapptz
"""

class ExponentialBackoff:
    """An implementation of the exponential backoff algorithm.

    Provides a convenient interface to implement an exponential backoff
    for reconnecting or retrying transmissions.

    Once instantiated, the delay method will return the next interval to
    wait for when retrying a connection or transmission. The maximum
    delay increases exponentially with each retry up to a maximum of
    2^10 * base.

    Raises
    ------
    :exc:`TimeoutError`
        Raised when the difference of time from the last request is
        greater than the client's timeout.
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
        """Compute the next delay.

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

        if self._timeout is not None and interval > self._timeout:
            raise TimeoutError('mojang')
            # self._exp = 0

        self._exp = min(self._exp + 1, self._max)
        return self._randfunc(0, self._base * 2**self._exp)
