"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass#, field
from typing import Tuple

__all__ = [
    'Leaderboard',
]


@dataclass
class Leaderboard:
    path: str
    prefix: str
    title: str
    location: Tuple[int, int, int]
    leaders: list

    def __post_init__(self):
        self.location.replace(', ', ',')
        self.location = tuple(self.location.split(','))

    # __iter__
    # __next__

# @dataclass
# class LeaderboardMode:
#     pass

# @dataclass(repr=False)
# class GameLeaderboard:
#     _data: dict = field(repr=False)
#     game: GameType = None
#     leaderboards: List[Leaderboard] = field(init=False)

#     def __post_init__(self):
#         self.leaderboards = None

    # __iter__
    # __next__

    # figure out stuff with classes idk
    # possibly:
    # Leaderboards[type_name].leaderboards[index] = leaderboard
    

    # def __post_init__(self):
    #     for mode in self._data:
    #         if 'Overall' in mode['prefix']:
    #             data = utils._clean(mode, mode='LB_OVERALL')
    #             setattr(self, data[])
    #         else:
    #             print('asdf')
