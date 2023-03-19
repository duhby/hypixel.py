"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

# Sorted alphabetically by category
__all__ = [
    'ARCADE',
    'BEDWARS',
    'BEDWARS_SOLO',
    'BEDWARS_DOUBLES',
    'BEDWARS_THREES',
    'BEDWARS_FOURS',
    'BEDWARS_TEAMS',
    'BLITZ',
    'CTW',
    'DUELS',
    'CLASSIC_DUELS',
    'COMBO_DUELS',
    'BLITZ_DUELS',
    'BOW_DUELS',
    'BOXING_DUELS',
    'BRIDGE_DUELS',
    'MEGA_WALLS_DUELS',
    'NO_DEBUFF_DUELS',
    'OP_DUELS',
    'PARKOUR_DUELS',
    'SKYWARS_DUELS',
    'SUMO_DUELS',
    'TNT_GAMES_DUELS',
    'UHC_DUELS',
    'HYPIXEL_SAYS',
    'MINI_WALLS',
    'MURDER_MYSTERY',
    'MM_ASSASSINS',
    'MM_CLASSIC',
    'MM_DOUBLE_UP',
    'MM_HARDCORE',
    'MM_SHOWDOWN',
    'PAINTBALL',
    'PARKOUR',
    'PARKOUR_LOBBY',
    'PARTY_GAMES',
    'SKYWARS',
    'SKYWARS_RANKED',
    'SKYWARS_SOLO_NORMAL',
    'SKYWARS_SOLO_INSANE',
    'SKYWARS_TEAM_NORMAL',
    'SKYWARS_TEAM_INSANE',
    'SKYWARS_MEGA_NORMAL',
    'SKYWARS_MEGA_DOUBLES',
    'SOCIALS',
    'TKR',
    'TNT_GAMES',
    'UHC',
    'UHC_SOLO',
    'UHC_TEAM',
    'UHC_BRAWL',
    # 'UHC_SOLO_BRAWL',
    # 'UHC_DUO_BRAWL',
    'WOOL_GAMES',
    'WOOL_GAMES_WOOL_WARS',
]


# Even if key-value pairs are equal, they still need to be added because
# values that don't have a key in the dictionary are skipped. All
# dataclasses should use an alias dictionary even if no modification is
# needed because if more variables are added to the API it will break.

ARCADE = {
    '_data': '_data',
    'coins': 'coins',
}

BEDWARS = {
    '_data': '_data',
    'bedwars_level': 'level',
    'coins': 'coins',
    'kills_bedwars': 'kills',
    'deaths_bedwars': 'deaths',
    'fall_deaths_bedwars': 'fall_deaths',
    'void_deaths_bedwars': 'void_deaths',
    'wins_bedwars': 'wins',
    'losses_bedwars': 'losses',
    'games_played_bedwars': 'games',
    'final_kills_bedwars': 'final_kills',
    'final_deaths_bedwars': 'final_deaths',
    'fall_final_deaths_bedwars': 'fall_final_deaths',
    'void_final_deaths_bedwars': 'void_final_deaths',
    'beds_broken_bedwars': 'beds_broken',
    'beds_lost_bedwars': 'beds_lost',
    'winstreak': 'winstreak',
    'Experience': 'exp',
    # 'activeIslandTopper': 'island_topper',
    # 'activeProjectileTrail': 'projectile_trail',
    # 'activeDeathCry': 'death_cry',
    # 'activeKillEffect': 'kill_effect',
    # 'selected_ultimate': 'selected_ultimate',
}

BEDWARS_SOLO = {
    'eight_one_kills_bedwars': 'kills',
    'eight_one_deaths_bedwars': 'deaths',
    'eight_one_fall_deaths_bedwars': 'fall_deaths',
    'eight_one_void_deaths_bedwars': 'void_deaths',
    'eight_one_wins_bedwars': 'wins',
    'eight_one_losses_bedwars': 'losses',
    'eight_one_games_played_bedwars': 'games',
    'eight_one_final_kills_bedwars': 'final_kills',
    'eight_one_final_deaths_bedwars': 'final_deaths',
    'eight_one_fall_final_deaths_bedwars': 'fall_final_deaths',
    'eight_one_void_final_deaths_bedwars': 'void_final_deaths',
    'eight_one_beds_broken_bedwars': 'beds_broken',
    'eight_one_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_DOUBLES = {
    'eight_two_kills_bedwars': 'kills',
    'eight_two_deaths_bedwars': 'deaths',
    'eight_two_fall_deaths_bedwars': 'fall_deaths',
    'eight_two_void_deaths_bedwars': 'void_deaths',
    'eight_two_wins_bedwars': 'wins',
    'eight_two_losses_bedwars': 'losses',
    'eight_two_games_played_bedwars': 'games',
    'eight_two_final_kills_bedwars': 'final_kills',
    'eight_two_final_deaths_bedwars': 'final_deaths',
    'eight_two_fall_final_deaths_bedwars': 'fall_final_deaths',
    'eight_two_void_final_deaths_bedwars': 'void_final_deaths',
    'eight_two_beds_broken_bedwars': 'beds_broken',
    'eight_two_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_THREES = {
    'four_three_kills_bedwars': 'kills',
    'four_three_deaths_bedwars': 'deaths',
    'four_three_fall_deaths_bedwars': 'fall_deaths',
    'four_three_void_deaths_bedwars': 'void_deaths',
    'four_three_wins_bedwars': 'wins',
    'four_three_losses_bedwars': 'losses',
    'four_three_games_played_bedwars': 'games',
    'four_three_final_kills_bedwars': 'final_kills',
    'four_three_final_deaths_bedwars': 'final_deaths',
    'four_three_fall_final_deaths_bedwars': 'fall_final_deaths',
    'four_three_void_final_deaths_bedwars': 'void_final_deaths',
    'four_three_beds_broken_bedwars': 'beds_broken',
    'four_three_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_FOURS = {
    'four_four_kills_bedwars': 'kills',
    'four_four_deaths_bedwars': 'deaths',
    'four_four_fall_deaths_bedwars': 'fall_deaths',
    'four_four_void_deaths_bedwars': 'void_deaths',
    'four_four_wins_bedwars': 'wins',
    'four_four_losses_bedwars': 'losses',
    'four_four_games_played_bedwars': 'games',
    'four_four_final_kills_bedwars': 'final_kills',
    'four_four_final_deaths_bedwars': 'final_deaths',
    'four_four_fall_final_deaths_bedwars': 'fall_final_deaths',
    'four_four_void_final_deaths_bedwars': 'void_final_deaths',
    'four_four_beds_broken_bedwars': 'beds_broken',
    'four_four_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_TEAMS = {
    'two_four_kills_bedwars': 'kills',
    'two_four_deaths_bedwars': 'deaths',
    'two_four_fall_deaths_bedwars': 'fall_deaths',
    'two_four_void_deaths_bedwars': 'void_deaths',
    'two_four_wins_bedwars': 'wins',
    'two_four_losses_bedwars': 'losses',
    'two_four_games_played_bedwars': 'games',
    'two_four_final_kills_bedwars': 'final_kills',
    'two_four_final_deaths_bedwars': 'final_deaths',
    'two_four_fall_final_deaths_bedwars': 'fall_final_deaths',
    'two_four_void_final_deaths_bedwars': 'void_final_deaths',
    'two_four_beds_broken_bedwars': 'beds_broken',
    'two_four_beds_lost_bedwars': 'beds_lost',
}

BLITZ = {
    'coins': 'coins',
    'kills': 'kills',
    'deaths': 'deaths',
    'wins': 'wins',
    'wins_solo_normal': 'wins_solo',
    'wins_team_normal': 'wins_team',
    'arrows_hit': 'arrows_hit',
    'arrows_fired': 'arrows_shot',
    'chests_opened': 'chests_opened',
    'games_played': 'games',
}

CTW = {
    'arcade_ctw_oh_sheep': 'captures',
    'arcade_ctw_slayer': 'kills_assists',
}

DUELS = {
    '_data': '_data',
    'coins': 'coins',
    'kills': 'kills',
    'deaths': 'deaths',
    'wins': 'wins',
    'losses': 'losses',
    'melee_hits': 'melee_hits',
    'melee_swings': 'melee_swings',
    'bow_hits': 'arrows_hit',
    'bow_shots': 'arrows_shot',
}

BLITZ_DUELS = {
    'blitz_duel_kills': 'kills',
    'blitz_duel_deaths': 'deaths',
    'blitz_duel_wins': 'wins',
    'blitz_duel_losses': 'losses',
    'blitz_duel_melee_hits': 'melee_hits',
    'blitz_duel_melee_swings': 'melee_swings',
    'blitz_duel_bow_hits': 'arrows_hit',
    'blitz_duel_bow_shots': 'arrows_shot',
}

BOW_DUELS = {
    'bow_duel_kills': 'kills',
    'bow_duel_deaths': 'deaths',
    'bow_duel_wins': 'wins',
    'bow_duel_losses': 'losses',
    # These give overall duels data for some reason...
    # 'bow_duel_melee_hits': 'melee_hits',
    # 'bow_duel_melee_swings': 'melee_swings',
    'bow_duel_bow_hits': 'arrows_hit',
    'bow_duel_bow_shots': 'arrows_shot',
}

BOXING_DUELS = {
    'boxing_duel_kills': 'kills',
    'boxing_duel_deaths': 'deaths',
    'boxing_duel_wins': 'wins',
    'boxing_duel_losses': 'losses',
    'boxing_duel_melee_hits': 'melee_hits',
    'boxing_duel_melee_swings': 'melee_swings',
    # 'boxing_duel_bow_hits': 'arrows_hit',
    # 'boxing_duel_bow_shots': 'arrows_shot',
}

BRIDGE_DUELS = {
    'bridge_duel_kills': 'kills',
    'bridge_duel_deaths': 'deaths',
    'bridge_duel_wins': 'wins',
    'bridge_duel_losses': 'losses',
    'bridge_duel_melee_hits': 'melee_hits',
    'bridge_duel_melee_swings': 'melee_swings',
    'bridge_duel_bow_hits': 'arrows_hit',
    'bridge_duel_bow_shots': 'arrows_shot',
}

# TODO: other bridge modes

CLASSIC_DUELS = {
    'classic_duel_kills': 'kills',
    'classic_duel_deaths': 'deaths',
    'classic_duel_wins': 'wins',
    'classic_duel_losses': 'losses',
    'classic_duel_melee_hits': 'melee_hits',
    'classic_duel_melee_swings': 'melee_swings',
    'classic_duel_bow_hits': 'arrows_hit',
    'classic_duel_bow_shots': 'arrows_shot',
}

COMBO_DUELS = {
    'combo_duel_kills': 'kills',
    'combo_duel_deaths': 'deaths',
    'combo_duel_wins': 'wins',
    'combo_duel_losses': 'losses',
    'combo_duel_melee_hits': 'melee_hits',
    'combo_duel_melee_swings': 'melee_swings',
    # 'combo_duel_bow_hits': 'arrows_hit',
    # 'combo_duel_bow_shots': 'arrows_shot',
}

MEGA_WALLS_DUELS = {
    'mega_walls_duel_kills': 'kills',
    'mega_walls_duel_deaths': 'deaths',
    'mega_walls_duel_wins': 'wins',
    'mega_walls_duel_losses': 'losses',
    'mega_walls_duel_melee_hits': 'melee_hits',
    'mega_walls_duel_melee_swings': 'melee_swings',
    'mega_walls_duel_bow_hits': 'arrows_hit',
    'mega_walls_duel_bow_shots': 'arrows_shot',
}

NO_DEBUFF_DUELS = {
    'no_debuff_duel_kills': 'kills',
    'no_debuff_duel_deaths': 'deaths',
    'no_debuff_duel_wins': 'wins',
    'no_debuff_duel_losses': 'losses',
    'no_debuff_duel_melee_hits': 'melee_hits',
    'no_debuff_duel_melee_swings': 'melee_swings',
    # 'no_debuff_duel_bow_hits': 'arrows_hit',
    # 'no_debuff_duel_bow_shots': 'arrows_shot',
}

OP_DUELS = {
    'op_duel_kills': 'kills',
    'op_duel_deaths': 'deaths',
    'op_duel_wins': 'wins',
    'op_duel_losses': 'losses',
    'op_duel_melee_hits': 'melee_hits',
    'op_duel_melee_swings': 'melee_swings',
    'op_duel_bow_hits': 'arrows_hit',
    'op_duel_bow_shots': 'arrows_shot',
}

PARKOUR_DUELS = {
    'parkour_duel_kills': 'kills',
    'parkour_duel_deaths': 'deaths',
    'parkour_duel_wins': 'wins',
    'parkour_duel_losses': 'losses',
    # 'parkour_duel_melee_hits': 'melee_hits',
    # 'parkour_duel_melee_swings': 'melee_swings',
    # 'parkour_duel_bow_hits': 'arrows_hit',
    # 'parkour_duel_bow_shots': 'arrows_shot',
}

SKYWARS_DUELS = {
    'skywars_duel_kills': 'kills',
    'skywars_duel_deaths': 'deaths',
    'skywars_duel_wins': 'wins',
    'skywars_duel_losses': 'losses',
    'skywars_duel_melee_hits': 'melee_hits',
    'skywars_duel_melee_swings': 'melee_swings',
    'skywars_duel_bow_hits': 'arrows_hit',
    'skywars_duel_bow_shots': 'arrows_shot',
}

# TODO: add other skywars gamemodes

SUMO_DUELS = {
    'sumo_duel_kills': 'kills',
    'sumo_duel_deaths': 'deaths',
    'sumo_duel_wins': 'wins',
    'sumo_duel_losses': 'losses',
    'sumo_duel_melee_hits': 'melee_hits',
    'sumo_duel_melee_swings': 'melee_swings',
    # 'sumo_duel_bow_hits': 'arrows_hit',
    # 'sumo_duel_bow_shots': 'arrows_shot',
}

TNT_GAMES_DUELS = {
    'tnt_games_duel_kills': 'kills',
    'tnt_games_duel_deaths': 'deaths',
    'tnt_games_duel_wins': 'wins',
    'tnt_games_duel_losses': 'losses',
    # 'tnt_games_duel_melee_hits': 'melee_hits',
    # 'tnt_games_duel_melee_swings': 'melee_swings',
    # 'tnt_games_duel_bow_hits': 'arrows_hit',
    'tnt_games_duel_bow_shots': 'arrows_shot',
}

UHC_DUELS = {
    'uhc_duel_kills': 'kills',
    'uhc_duel_deaths': 'deaths',
    'uhc_duel_wins': 'wins',
    'uhc_duel_losses': 'losses',
    'uhc_duel_melee_hits': 'melee_hits',
    'uhc_duel_melee_swings': 'melee_swings',
    'uhc_duel_bow_hits': 'arrows_hit',
    'uhc_duel_bow_shots': 'arrows_shot',
}

HYPIXEL_SAYS = {
    'rounds_simon_says': 'rounds',
    'wins_simon_says': 'wins',
    'top_score_simon_says': 'top_score',
}

MINI_WALLS = {
    'kills_mini_walls': 'kills',
    'deaths_mini_walls': 'deaths',
    'wins_mini_walls': 'wins',
    'final_kills_mini_walls': 'final_kills',
    'wither_kills_mini_walls': 'wither_kills',
    'wither_damage_mini_walls': 'wither_damage',
    'arrows_hit_mini_walls': 'arrows_hit',
    'arrows_shot_mini_walls': 'arrows_shot',
}

MURDER_MYSTERY = {
    '_data': '_data',
    'coins': 'coins',
    'games': 'games',
    'wins': 'wins',
    'kills': 'kills',
    'deaths': 'deaths',
    'bow_kills': 'bow_kills',
    'knife_kills': 'knife_kills',
    'thrown_knife_kills': 'thrown_knife_kills',
    'murderer_wins': 'murderer_wins',
    'detective_wins': 'detective_wins',
}

MM_ASSASSINS = {
    'games_MURDER_ASSASSINS': 'games',
    'wins_MURDER_ASSASSINS': 'wins',
    'kills_MURDER_ASSASSINS': 'kills',
    'deaths_MURDER_ASSASSINS': 'deaths',
    'bow_kills_MURDER_ASSASSINS': 'bow_kills',
    'knife_kills_MURDER_ASSASSINS': 'knife_kills',
    'thrown_knife_kills_MURDER_ASSASSINS': 'thrown_knife_kills',
}

MM_CLASSIC = {
    'games_MURDER_CLASSIC': 'games',
    'wins_MURDER_CLASSIC': 'wins',
    'kills_MURDER_CLASSIC': 'kills',
    'deaths_MURDER_CLASSIC': 'deaths',
    'bow_kills_MURDER_CLASSIC': 'bow_kills',
    'knife_kills_MURDER_CLASSIC': 'knife_kills',
    'thrown_knife_kills_MURDER_CLASSIC': 'thrown_knife_kills',
}

MM_DOUBLE_UP = {
    'games_MURDER_DOUBLE_UP': 'games',
    'wins_MURDER_DOUBLE_UP': 'wins',
    'kills_MURDER_DOUBLE_UP': 'kills',
    'deaths_MURDER_DOUBLE_UP': 'deaths',
    'bow_kills_MURDER_DOUBLE_UP': 'bow_kills',
    'knife_kills_MURDER_DOUBLE_UP': 'knife_kills',
    'thrown_knife_kills_MURDER_DOUBLE_UP': 'thrown_knife_kills',
}

MM_HARDCORE = {
    'games_MURDER_HARDCORE': 'games',
    'wins_MURDER_HARDCORE': 'wins',
    'kills_MURDER_HARDCORE': 'kills',
    'deaths_MURDER_HARDCORE': 'deaths',
    'bow_kills_MURDER_HARDCORE': 'bow_kills',
    'knife_kills_MURDER_HARDCORE': 'knife_kills',
    'thrown_knife_kills_MURDER_HARDCORE': 'thrown_knife_kills',
    'removed': 'removed',
}

MM_SHOWDOWN = {
    'games_MURDER_SHOWDOWN': 'games',
    'wins_MURDER_SHOWDOWN': 'wins',
    'kills_MURDER_SHOWDOWN': 'kills',
    'deaths_MURDER_SHOWDOWN': 'deaths',
    'bow_kills_MURDER_SHOWDOWN': 'bow_kills',
    'knife_kills_MURDER_SHOWDOWN': 'knife_kills',
    'thrown_knife_kills_MURDER_SHOWDOWN': 'thrown_knife_kills',
    'removed': 'removed',
}

PAINTBALL = {
    'coins': 'coins',
    'wins': 'wins',
    'kills': 'kills',
    'deaths': 'deaths',
    'killstreaks': 'killstreaks',
    'shots_fired': 'shots_fired',
}

PARKOUR = {
    '_data': '_data',
    'ArcadeGames': 'arcade',
    'Bedwars': 'bedwars',
    'BlitzLobby': 'blitz',
    'BuildBattle': 'build_battle',
    'CopsnCrims': 'cops_and_crims',
    'Duels': 'duels',
    'mainLobby2017': 'main',
    'MegaWalls': 'mega_walls',
    'MurderMystery': 'murder_mystery',
    # 'Paintball': 'paintball',
    'SkywarsAug2017': 'skywars',
    'SuperSmash': 'smash',
    'TNT': 'tnt',
    'uhc': 'uhc',
    'Warlords': 'warlords',
}

PARKOUR_LOBBY = {
    'timeStart': 'completed',
    'timeTook': 'time',
}

PARTY_GAMES = {
    'wins_party': 'wins',
    'wins_party_2': 'wins_2',
    'wins_party_3': 'wins_3',
}

SKYWARS = {
    '_data': '_data',
    'coins': 'coins',
    'kills': 'kills',
    'deaths': 'deaths',
    'wins': 'wins',
    'losses': 'losses',
    'games': 'games',
    'arrows_hit': 'arrows_hit',
    'arrows_shot': 'arrows_shot',
    'win_streak': 'winstreak',
    'souls': 'souls',
    'skywars_experience': 'exp',
}

SKYWARS_RANKED = {
    'kills_ranked': 'kills',
    'deaths_ranked': 'deaths',
    'wins_ranked': 'wins',
    'losses_ranked': 'losses',
}

SKYWARS_SOLO_NORMAL = {
    'kills_solo_normal': 'kills',
    'deaths_solo_normal': 'deaths',
    'wins_solo_normal': 'wins',
    'losses_solo_normal': 'losses',
}

SKYWARS_SOLO_INSANE = {
    'kills_solo_insane': 'kills',
    'deaths_solo_insane': 'deaths',
    'wins_solo_insane': 'wins',
    'losses_solo_insane': 'losses',
}

SKYWARS_TEAM_NORMAL = {
    'kills_team_normal': 'kills',
    'deaths_team_normal': 'deaths',
    'wins_team_normal': 'wins',
    'losses_team_normal': 'losses',
}

SKYWARS_TEAM_INSANE = {
    'kills_team_insane': 'kills',
    'deaths_team_insane': 'deaths',
    'wins_team_insane': 'wins',
    'losses_team_insane': 'losses',
}

SKYWARS_MEGA_NORMAL = {
    'kills_mega_normal': 'kills',
    'deaths_mega_normal': 'deaths',
    'wins_mega_normal': 'wins',
    'losses_mega_normal': 'losses',
}

SKYWARS_MEGA_DOUBLES = {
    'kills_mega_doubles': 'kills',
    'deaths_mega_doubles': 'deaths',
    'wins_mega_doubles': 'wins',
    'losses_mega_doubles': 'losses',
}

SOCIALS = {
    'DISCORD': 'discord',
    'YOUTUBE': 'youtube',
    'TWITTER': 'twitter',
    'TWITCH': 'twitch',
    'INSTAGRAM': 'instagram',
    'HYPIXEL': 'hypixel_forums',
}

TKR = {
    'coins': 'coins',
    'laps_completed': 'laps',
    'gold_trophy': 'gold',
    'silver_trophy': 'silver',
    'bronze_trophy': 'bronze',
    'blue_torpedo_hit': 'blue_torpedo_hits',
    'banana_hits_sent': 'banana_hits',
    'banana_hits_received': 'bananas_received',
    # 'box_pickups': 'powerups',
    'wins': 'wins',
}

TNT_GAMES = {
    'coins': 'coins',
}

UHC = {
    '_data': '_data',
    'coins': 'coins',
    'score': 'score',
    'uhc_parkour_1': 'parkour_1',
    'uhc_parkour_2': 'parkour_2',
}

UHC_SOLO = {
    'wins_solo': 'wins',
    'kills_solo': 'kills',
    'deaths_solo': 'deaths',
    'heads_eaten_solo': 'heads_eaten',
    'ultimates_crafted_solo': 'ultimates_crafted',
}

UHC_TEAM = {
    'wins': 'wins',
    'kills': 'kills',
    'deaths': 'deaths',
    'heads_eaten': 'heads_eaten',
    'ultimates_crafted': 'ultimates_crafted',
}

UHC_BRAWL = {
    'wins_brawl': 'wins',
    'kills_brawl': 'kills',
    'deaths_brawl': 'deaths',
    'heads_eaten_brawl': 'heads_eaten',
    'ultimates_crafted_brawl': 'ultimates_crafted',
}

# UHC_SOLO_BRAWL = {
#     'wins_solo brawl': 'wins',
#     'kills_solo brawl': 'kills',
#     'deaths_solo brawl': 'deaths',
#     'heads_eaten_solo brawl': 'heads_eaten',
#     'ultimates_crafted_solo brawl': 'ultimates_crafted',
# }

# UHC_DUO_BRAWL = {
#     'wins_duo brawl': 'wins',
#     'kills_duo brawl': 'kills',
#     'deaths_duo brawl': 'deaths',
#     'heads_eaten_duo brawl': 'heads_eaten',
#     'ultimates_crafted_duo brawl': 'ultimates_crafted',
# }

WOOL_GAMES = {
    '_data': '_data',
    'level': 'level',
    'coins': 'coins',
    'experience': 'exp'
}

WOOL_GAMES_WOOL_WARS = {
    'kills': 'kills',
    'deaths': 'deaths',
    'assists': 'assists',
    'wins': 'wins',
    'games_played': 'games',
    'blocks_broken': 'blocks_broken',
    'wool_placed': 'wool_placed',
    'selected_class': 'selected_class',
}
