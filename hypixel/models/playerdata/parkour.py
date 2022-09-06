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
from datetime import datetime, timedelta

from ... import utils

__all__ = (
    'ParkourLobby',
    'Parkour',
)

@dataclass
class ParkourLobby:
    completed: datetime
    time: timedelta

    def __post_init__(self):
        self.time = timedelta(seconds=(self.time / 1e3))
        self.completed = utils.convert_to_datetime(
            self.completed
        ) + self.time

# Only has the main 14 parkours
@dataclass
class Parkour:
    _data: dict = field(repr=False)
    arcade: ParkourLobby = field(init=False)
    bedwars: ParkourLobby = field(init=False)
    blitz: ParkourLobby = field(init=False)
    build_battle: ParkourLobby = field(init=False)
    cops_and_crims: ParkourLobby = field(init=False)
    duels: ParkourLobby = field(init=False)
    main: ParkourLobby = field(init=False)
    mega_walls: ParkourLobby = field(init=False)
    murder_mystery: ParkourLobby = field(init=False)
    # paintball: ParkourLobby = field(init=False)
    skywars: ParkourLobby = field(init=False)
    smash: ParkourLobby = field(init=False)
    tnt: ParkourLobby = field(init=False)
    uhc: ParkourLobby = field(init=False)
    warlords: ParkourLobby = field(init=False)

    def __post_init__(self):
        self._modes = (
            'arcade',
            'bedwars',
            'blitz',
            'build_battle',
            'cops_and_crims',
            'duels',
            'main',
            'mega_walls',
            'murder_mystery',
            # 'paintball',
            'skywars',
            'smash',
            'tnt',
            'uhc',
            'warlords',
        )
        self._len = len(self._modes)
        for mode in self._modes:
            data = self._data.get(mode)
            if data:
                data = utils._clean(data[0], mode='PARKOUR_LOBBY')
                setattr(self, mode, ParkourLobby(**data))
                continue
            setattr(self, mode, None)

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i < self._len:
            result = getattr(self, self._modes[self._i])
            self._i += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('indices must be integers')
        if index < self._len:
            return getattr(self, self._modes[index])
        else:
            raise IndexError('index out of range')

    def __len__(self):
        return self._len
