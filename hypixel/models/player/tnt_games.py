"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass#, field

# from . import utils

__all__ = [
    'TntGames',
]


@dataclass
class TntGames:
    coins: int = 0
