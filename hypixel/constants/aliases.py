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
    'achievementPoints': 'achievement_points',
    'networkExp': 'network_exp',
    'karma': 'karma',
    'mcVersionRp': 'version',
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
}

GAMEMODES = {
    'bedwars': BEDWARS,
}
