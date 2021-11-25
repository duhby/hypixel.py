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

from typing import Dict, Union
from aiohttp import ClientSession

from .constants import aliases

def _clean(data: Dict, mode='PLAYER') -> Dict:
    alias = getattr(aliases, mode)
    if mode == 'PLAYER':
        # avoid name conflicts
        data['achievement_stats'] = data.pop('achievements', {})
    elif mode == 'BEDWARS':
        _data = dict(data)
        level = data.get('achievement_stats', {}).get('bedwars_level')
        data = data.get('stats', {}).get('Bedwars', {})
        data['bedwars_level'] = level
        data['_data'] = _data
    elif mode in ('ARCADE', 'HYPIXEL_SAYS', 'PARTY_GAMES'):
        _data = dict(data)
        data = data.get('stats', {}).get('Arcade', {})
        data['_data'] = _data
    elif 'BEDWARS' in mode:
        data = data.get('stats', {}).get('Bedwars', {})
    elif mode == 'CTW':
        data = data.get('achievement_stats', {})
    elif mode == 'TKR':
        data = data.get('stats', {}).get('GingerBread', {})
    # replace keys in data with their formatted alias
    replaced_data = {alias.get(k, k): v for k, v in data.items()}
    # remove unused/unsupported items
    return {key: replaced_data[key] for key in replaced_data if key in alias.values()}

def get_level(network_exp: int) -> float:
    return round(1 + (-8750.0 + (8750 ** 2 + 5000 * network_exp) ** 0.5) / 2500, 2)

async def _get_uuid(session: ClientSession, name: str) -> str:
    try:
        response = await session.get(f'https://api.mojang.com/users/profiles/minecraft/{name}')
        # TODO: add response error handling
        response = await response.json()
        return response.get('id')
    except Exception:
        raise ValueError

def safe_div(a: int, b: int) -> float:
    if not b:
        return a
    else:
        return round(a / b, 2)

COLORS = ('§0', '§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8', '§9', '§a', '§b', '§c', '§d', '§e', '§f')
def clean_rank_prefix(string: str) -> str:
    for color in COLORS:
        string = string.replace(color, '')
    string = string.replace('[', '').replace(']', '')
    return string
