"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field
from typing import Optional

from ..game import Game

__all__ = [
    'Status',
]


@dataclass
class Status:
    raw: dict = field(repr=False)
    online: bool = False # False if the player has status disabled
    game_type: Optional[Game] = None
    mode: Optional[str] = None # TODO: make this a type
    map: Optional[str] = None # TODO: make this a type
