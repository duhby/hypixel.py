"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field

__all__ = [
    'Bans',
]


@dataclass
class Bans:
    raw: dict = field(repr=False)
    staff_day: int
    staff_total: int
    watchdog_recent: int # past minute
    watchdog_day: int
    watchdog_total: int
