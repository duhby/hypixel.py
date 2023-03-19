"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

# Sorted alphabetically by category
__all__ = [
    'ACHIEVEMENT',
    'BANS',
    # 'FRIEND',
    'GUILD',
    'KEY',
    'LB',
    'PLAYER',
    'STATUS',
]


# Even if key-value pairs are equal, they still need to be added because
# values that don't have a key in the dictionary are skipped. All
# dataclasses should use an alias dictionary even if no modification is
# needed because if more variables are added to the API it will break.

ACHIEVEMENT = {
    'type_name': 'type_name',
    'points': 'points',
    'name': 'name',
    'description': 'description',
    'globalPercentUnlocked': 'global_unlocked',
    'gamePercentUnlocked': 'game_unlocked',
    'legacy': 'legacy',
}

BANS = {
    'staff_rollingDaily': 'staff_day',
    'staff_total': 'staff_total',
    'watchdog_lastMinute': 'watchdog_recent',
    'watchdog_rollingDaily': 'watchdog_day',
    'watchdog_total': 'watchdog_total',
}

# Deprecated by Hypixel
# FRIEND = {
#     '_id': 'id',
#     'uuidReceiver': 'uuid',
#     'started': 'started',
# }

GUILD = {
    '_id': 'id',
    'name': 'name',
    'exp': 'exp',
    'created': 'created',
    'winners': 'winners',
    'experience_kings': 'experience_kings',
    'most_online_players': 'most_online_players',
    'legacyRanking': 'legacy_rank',
    'members': 'members',
    'ranks': 'ranks',
    'joinable': 'joinable',
    'tag': 'tag',
    'tagColor': 'tag_color',
    'description': 'description',
    'preferredGames': 'preferred_games',
    'publiclyListed': 'publicly_listed',
    'guildExpByGameType': 'game_exp',
    # 'banner': 'banner',
}

KEY = {
    'key': 'key',
    'owner': 'owner',
    'limit': 'limit',
    'totalQueries': 'queries',
    'queriesInPastMin': 'recent_queries',
}

LB = {
    'path': 'path',
    'prefix': 'prefix',
    'title': 'title',
    'location': 'location',
    'leaders': 'leaders',
}

PLAYER = {
    '_id': 'id',
    'uuid': 'uuid',
    'firstLogin': 'first_login',
    'displayname': 'name',
    # Lowercase version of displayname, so basically useless
    # 'playername'
    'lastLogin': 'last_login',
    'lastLogout': 'last_logout',
    'achievementsOneTime': 'achievements',
    # 'achievement_stats'
    'achievementPoints': 'achievement_points',
    'networkExp': 'network_exp',
    'karma': 'karma',
    'currentGadget': 'current_gadget',
    'channel': 'channel',
    # 'rankPlusColor'
    # 'monthlyPackageRank'
    # 'monthlyRankColor'
    # 'lastAdsenseGenerateTime'
    # 'lastClaimedReward'
    # 'totalRewards'
    # 'totalDailyRewards'
    # 'rewardStreak'
    # 'rewardScore'
    # 'rewardHighScore'
    # 'friendRequestsUuid'
    # 'achievementTracking'

    # Handled in Player class instead
    # 'mostRecentGameType'
    # 'rank'
    # 'newPackageRank'

    # Deprecated by hypixel
    # 'knownAliases'
    # 'knownAliasesLower'
    # 'mcVersionRp'
}

STATUS = {
    'online': 'online',
    'gameType': 'game',
    'mode': 'mode',
    'map': 'map',
}
