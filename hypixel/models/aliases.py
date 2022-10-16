"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

# Sorted alphabetically by category
__all__ = [
    'GUILD_MEMBER',
    'GUILD_RANK',
]


# Even if key-value pairs are equal, they still need to be added because
# values that don't have a key in the dictionary are skipped. All
# dataclasses should use an alias dictionary even if no modification is
# needed because if more variables are added to the API it will break.

GUILD_MEMBER = {
    'uuid': 'uuid',
    'rank': 'rank',
    'joined': 'joined',
    'expHistory': 'exp_history',
    'questParticipation': 'quest_participation',
    'name': 'name',
}

GUILD_RANK = {
    'name': 'name',
    'default': 'default',
    'created': 'created',
    'priority': 'priority',
    'tag': 'tag',
}
