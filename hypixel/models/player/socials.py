"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass
from typing import Optional

__all__ = [
    'Socials',
]


@dataclass
class Socials:
    discord: Optional[str] = None
    youtube: Optional[str] = None
    twitter: Optional[str] = None
    twitch: Optional[str] = None
    instagram: Optional[str] = None
    hypixel_forums: Optional[str] = None
