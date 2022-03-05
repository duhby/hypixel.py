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

REQUIRE_COPY = (
    'ARCADE',
    'DUELS',
    'HYPIXEL_SAYS',
    'MINI_WALLS',
    'PARTY_GAMES',
)

# even if key-value pairs are equal, they still need to be added because
# values that don't have a key in the dictionary are skipped

KEY = {
    'key': 'key',
    'owner': 'owner',
    'limit': 'limit',
    'totalQueries': 'queries',
    'queriesInPastMin': 'recent_queries',
}

PLAYER = {
    '_id': 'id',
    'uuid': 'uuid',
    'firstLogin': 'first_login',
    'displayname': 'name',
    # 'playername': 'name', # lowercase version of displayname
    'lastLogin': 'last_login',
    'lastLogout': 'last_logout',
    'knownAliases': 'known_aliases',
    # 'knownAliasesLower'
    'achievementsOneTime': 'achievements',
    # 'achievement_stats': 'achievement_stats',
    'achievementPoints': 'achievement_points',
    'networkExp': 'network_exp',
    'karma': 'karma',
    'mcVersionRp': 'version',
    # 'rank': 'rank_',
    # 'newPackageRank': 'package_rank',
    # 'rankPlusColor': 'rank_color',
    # 'monthlyPackageRank': 'monthly_package_rank',
    # 'monthlyRankColor': 'monthly_rank_color',
    # 'lastAdsenseGenerateTime'
    # 'lastClaimedReward'
    # 'totalRewards'
    # 'totalDailyRewards'
    # 'rewardStreak'
    # 'rewardScore'
    # 'rewardHighScore'
    # 'friendRequestsUuid': 'friend_requests_uuid'
    # 'achievementTracking'
    'currentGadget': 'current_gadget',
    'channel': 'channel',
    'mostRecentGameType': 'most_recent_game',
}

BEDWARS = {
    '_data': '_data',
    'bedwars_level': 'level',
    'coins': 'coins',
    'kills_bedwars': 'kills',
    'deaths_bedwars': 'deaths',
    'wins_bedwars': 'wins',
    'losses_bedwars': 'losses',
    'games_played_bedwars': 'games_played',
    'final_kills_bedwars': 'final_kills',
    'final_deaths_bedwars': 'final_deaths',
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
    'eight_one_wins_bedwars': 'wins',
    'eight_one_losses_bedwars': 'losses',
    'eight_one_games_played_bedwars': 'games_played',
    'eight_one_final_kills_bedwars': 'final_kills',
    'eight_one_final_deaths_bedwars': 'final_deaths',
    'eight_one_beds_broken_bedwars': 'beds_broken',
    'eight_one_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_DOUBLES = {
    'eight_two_kills_bedwars': 'kills',
    'eight_two_deaths_bedwars': 'deaths',
    'eight_two_wins_bedwars': 'wins',
    'eight_two_losses_bedwars': 'losses',
    'eight_two_games_played_bedwars': 'games_played',
    'eight_two_final_kills_bedwars': 'final_kills',
    'eight_two_final_deaths_bedwars': 'final_deaths',
    'eight_two_beds_broken_bedwars': 'beds_broken',
    'eight_two_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_THREES = {
    'four_three_kills_bedwars': 'kills',
    'four_three_deaths_bedwars': 'deaths',
    'four_three_wins_bedwars': 'wins',
    'four_three_losses_bedwars': 'losses',
    'four_three_games_played_bedwars': 'games_played',
    'four_three_final_kills_bedwars': 'final_kills',
    'four_three_final_deaths_bedwars': 'final_deaths',
    'four_three_beds_broken_bedwars': 'beds_broken',
    'four_three_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_FOURS = {
    'four_four_kills_bedwars': 'kills',
    'four_four_deaths_bedwars': 'deaths',
    'four_four_wins_bedwars': 'wins',
    'four_four_losses_bedwars': 'losses',
    'four_four_games_played_bedwars': 'games_played',
    'four_four_final_kills_bedwars': 'final_kills',
    'four_four_final_deaths_bedwars': 'final_deaths',
    'four_four_beds_broken_bedwars': 'beds_broken',
    'four_four_beds_lost_bedwars': 'beds_lost',
}

BEDWARS_TEAMS = {
    'two_four_kills_bedwars': 'kills',
    'two_four_deaths_bedwars': 'deaths',
    'two_four_wins_bedwars': 'wins',
    'two_four_losses_bedwars': 'losses',
    'two_four_games_played_bedwars': 'games_played',
    'two_four_final_kills_bedwars': 'final_kills',
    'two_four_final_deaths_bedwars': 'final_deaths',
    'two_four_beds_broken_bedwars': 'beds_broken',
    'two_four_beds_lost_bedwars': 'beds_lost',
}

ARCADE = {
    '_data': '_data',
    'coins': 'coins',
}

CTW = {
    'arcade_ctw_oh_sheep': 'captures',
    'arcade_ctw_slayer': 'kills_assists',
}

HYPIXEL_SAYS = {
    'rounds_simon_says': 'rounds',
    'wins_simon_says': 'wins',
}

PARTY_GAMES = {
    'wins_party': 'wins',
    'wins_party_2': 'wins_2',
    'wins_party_3': 'wins_3',
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

TKR = {
    'coins': 'coins',
    'laps_completed': 'laps',
    'gold_trophy': 'gold',
    'silver_trophy': 'silver',
    'bronze_trophy': 'bronze',
    'blue_torpedo_hit': 'blue_torpedo_hits',
    'banana_hits_sent': 'banana_hits',
    'banana_hits_received': 'bananas_received',
    'wins': 'wins',
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
    # why if these are uncommented does it give overall duels data?
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

# somehow I don't need to rename anything what
PAINTBALL = {
    'coins': 'coins',
    'wins': 'wins',
    'kills': 'kills',
    'deaths': 'deaths',
    'killstreaks': 'killstreaks',
    'shots_fired': 'shots_fired',
}

SOCIALS = {
    'DISCORD': 'discord',
    'YOUTUBE': 'youtube',
    'TWITTER': 'twitter',
    'TWITCH': 'twitch',
    'INSTAGRAM': 'instagram',
    'HYPIXEL': 'hypixel_forums',
}

BANS = {
    'staff_rollingDaily': 'staff_day',
    'staff_total': 'staff_total',
    'watchdog_lastMinute': 'watchdog_recent',
    'watchdog_rollingDaily': 'watchdog_day',
    'watchdog_total': 'watchdog_total',
}

FRIEND = {
    '_id': 'id',
    'uuidReceiver': 'uuid',
    'started': 'started',
}

STATUS = {
    'online': 'online',
    'gameType': 'game_type',
    'mode': 'mode',
    'map': 'map',
}
