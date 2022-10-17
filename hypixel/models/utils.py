"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from datetime import datetime, timezone

from .aliases import *
from .guild import GuildRank


def _clean(data: dict, mode: str, extra=None) -> dict:
    alias = globals()[mode]

    if mode == 'GUILD_MEMBER':
        # Extra is the guild's ranks.
        rank = next((
            rank for rank in extra if rank.name == data['rank']
        ), None)
        if rank is not None:
            data['rank'] = rank
        else:
            # TODO: get a list of legacy ranks like Guild Master and
            # Officer.
            data['rank'] = GuildRank(name=data['rank'])

    # Replace keys in data with formatted alias
    # Remove items that are not in the alias dictionary
    return {alias.get(k, k): v for k, v in data.items() if k in alias.keys()}

def convert_to_datetime(decimal: int) -> datetime:
    # Float division is cheaper than integer division.
    # Precision is a non-issue as decimals go only to the thousandth
    # place.
    seconds = decimal / 1e3
    dt = datetime.fromtimestamp(seconds, tz=timezone.utc)
    return dt

# Length 15
xps_g = (100000, 150000, 250000, 500000, 750000, 1000000, 1250000, 1500000,
              2000000, 2500000, 2500000, 2500000, 2500000, 2500000, 3000000)
MAX_LEVEL = 1000
def guild_level(exp: int) -> float:
    level = 0
    for i in range(MAX_LEVEL + 1):
        # Required exp to get to the next level
        need = 0
        if i >= 15:
            need = xps_g[-1]
        else:
            need = xps_g[i]

        # Return the current level plus progress towards the next
        # (unused) if the required exp is met. Otherwise, increment the
        # level and subtract the used exp.
        if exp - need < 0:
            return round((level + (exp / need)) * 100) / 100
        level += 1
        exp -= need
    return MAX_LEVEL
