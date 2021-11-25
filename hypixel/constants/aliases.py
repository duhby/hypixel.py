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
    
    # 'particle_trail': 'particle_trail',
}

SOCIALS = {
    'DISCORD': 'discord',
    'YOUTUBE': 'youtube',
    'TWITTER': 'twitter',
    'TWITCH': 'twitch',
    'INSTAGRAM': 'instagram',
    'HYPIXEL': 'hypixel_forums',
}
