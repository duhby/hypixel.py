"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

__all__ = [
    'Key',
]


@dataclass
class Key:
    raw: dict = field(repr=False)
    key: str
    owner: str # uuid
    limit: int # per minute
    queries: int = 0
    recent_queries: int = 0 # past minue
