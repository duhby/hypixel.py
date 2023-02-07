"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from datetime import datetime, timezone

from .aliases import *


REQUIRE_COPY = [
    'ARCADE',
    'HYPIXEL_SAYS',
    'MINI_WALLS',
    'PARTY_GAMES',
]
def _clean(data: dict, mode: str) -> dict:
    alias = globals()[mode]

    if mode in REQUIRE_COPY:
        _data = data.copy()

    if mode == 'ARCADE':
        data = data.get('stats', {}).get('Arcade', {})

    elif mode == 'SOCIALS':
        data = data.get('socialMedia', {}).get('links', {})

    elif mode in ('HYPIXEL_SAYS', 'MINI_WALLS', 'PARTY_GAMES'):
        data = data.get('stats', {}).get('Arcade', {})

    elif mode == 'TKR':
        data = data.get('stats', {}).get('GingerBread', {})

    elif mode == 'MURDER_MYSTERY':
        data = data.get('stats', {}).get('MurderMystery', {})
        data['_data'] = data.copy()

    elif mode == 'UHC':
        data = data.get('stats', {}).get('UHC', {})
        data['_data'] = data.copy()

    elif mode == 'BEDWARS':
        level = data.get('achievement_stats', {}).get('bedwars_level', 1)
        data = data.get('stats', {}).get('Bedwars', {})
        data['bedwars_level'] = level
        # Copy here instead of before and after because BedwarsMode
        # classes need stats.Bedwars specific data.
        data['_data'] = data.copy()

    elif mode == 'SKYWARS':
        data = data.get('stats', {}).get('SkyWars', {})
        # Copy here instead of before and after because SkywarsMode
        # classes need stats.SkyWars specific data.
        data['_data'] = data.copy()

    elif mode == 'DUELS':
        data = data.get('stats', {}).get('Duels', {})
        # Copy here instead of before and after because DuelsMode
        # classes need stats.Duels specific data.
        data['_data'] = data.copy()

    elif mode == 'PAINTBALL':
        data = data.get('stats', {}).get('Paintball', {})

    elif mode == 'PARKOUR':
        # Return here because _data is used after aliases are converted
        data = data.get('parkourCompletions', {})
        replaced_data = {alias.get(k, k): v for k, v in data.items()}
        data = {
            key: replaced_data[key]
            for key in replaced_data if key in alias.values()
        }
        return {'_data': data}

    elif mode == 'BLITZ':
        data = data.get('stats', {}).get('HungerGames', {})

    elif mode == 'TNT_GAMES':
        data = data.get('stats', {}).get('TNTGames', {})

    elif mode == 'CTW':
        data = data.get('achievement_stats', {})

    elif mode in ('MM_HARDCORE', 'MM_SHOWDOWN'):
        data['removed'] = True

    elif mode == 'WOOL_GAMES':
        data = data.get('stats', {}).get('WoolGames', {})
        data['experience'] = round(data.get('progression', {}).get('experience', 0))
        # Copy here instead of before and after because WoolGamesMode
        # classes need stats.WoolGames specific data.
        data['_data'] = data.copy()

    elif mode == 'WOOL_GAMES_WOOL_WARS':
        selected_class = data.get('wool_wars', {}).get('selected_class')
        data = data.get('wool_wars', {}).get('stats', {})
        data['selected_class'] = selected_class

    if mode in REQUIRE_COPY:
        data['_data'] = _data

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

def get_network_level(network_exp: int) -> float:
    return round(1 + (-8750.0 + (8750 ** 2 + 5000 * network_exp) ** 0.5) / 2500, 2)

# Same calculation as bedwars experience to bedwars level
def get_wool_wars_level(exp: int) -> float:
    levels = (exp // 487000) * 100
    exp %= 487000

    costs = {1: 500, 2: 1000, 3: 2000, 4: 3500}
    for i in range(1, 5):
        cost = costs[i]
        if exp >= cost:
            levels += 1
            exp -= cost
        else:
            break

    levels += exp // 5000
    exp %= 5000

    next_level = (levels + 1) % 100

    if next_level in costs:
        next_level_cost = costs[next_level]
    else:
        next_level_cost = 5000

    return round(levels + exp / next_level_cost, 2)

def safe_div(a: int, b: int) -> float:
    if not b:
        return float(a)
    else:
        return round(a / b, 2)

# Values past 10 aren't used, but this still works up to 40.
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

colors = ('§0', '§1', '§2', '§3', '§4', '§5', '§6', '§7',
          '§8', '§9', '§a', '§b', '§c', '§d', '§e', '§f')
def clean_rank_prefix(string: str) -> str:
    # .replace is faster than re.sub
    for color in colors:
        string = string.replace(color, '')
    string = string.replace('[', '').replace(']', '')
    return string

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


"""
MIT License

Copyright (c) 2018 The Slothpixel Project
"""

# Length 12
xps_s = (0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000)
def skywars_level(exp) -> float:
    if exp >= 15000:
        return (exp - 15000) / 10000 + 12
    for i in range(12):
        if exp < xps_s[i]:
            return i + (exp - xps_s[i - 1]) / (xps_s[i] - xps_s[i - 1])

xps_u = (0, 10, 60, 210, 460, 960, 1710, 2710, 5210, 10210, 13210, 16210,
       19210, 22210, 25210)
def uhc_level(exp):
    level = 0
    for xp in xps_u:
        if exp >= xp:
            level += 1
        else:
            break
    return level
