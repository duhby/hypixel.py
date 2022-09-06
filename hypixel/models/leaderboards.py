"""
The MIT License

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

from dataclasses import dataclass, field
from typing import Tuple

__all__ = (
    'Leaderboard',
)

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
