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

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime

from typing import Dict, List, Literal, Optional
from .games import GameType
from ..constants import GameTypes
from .color import ColorType

from .. import utils

__all__ = (
    'Guild',
    'GuildMember',
    'GuildRank',
)

@dataclass
class GuildRank:
    name: str
    default: bool = False
    created: Optional[datetime] = None
    priority: Optional[int] = None
    tag: Optional[str] = None

    def __post_init__(self):
        if self.created is not None:
            self.created = utils.convert_to_datetime(self.created)

@dataclass
class GuildMember:
    uuid: str
    rank: GuildRank
    joined: datetime
    exp_history: Dict[datetime, int] = field(repr=False)
    quest_participation: int = 0
    name: Optional[str] = None # legacy

    def __post_init__(self):
        self.joined = utils.convert_to_datetime(self.joined)

        self.exp_history = {
            utils._add_tzinfo(datetime.strptime(time, '%Y-%m-%d')): value
            for time, value in self.exp_history.items()
        }

@dataclass
class Guild:
    raw: dict = field(repr=False)
    id: str
    name: str
    exp: int
    created: datetime
    level: int = None # handled later
    legacy_rank: Optional[int] = None
    members: List[GuildMember] = field(default_factory=list)
    ranks: List[GuildRank] = field(default_factory=list)
    winners: int = 0
    experience_kings: int = 0
    most_online_players: int = 0
    joinable: bool = False
    tag: Optional[str] = None
    tag_color: Optional[ColorType] = None
    description: Optional[str] = None
    preferred_games: List[GameType] = field(default_factory=list)
    publicly_listed: bool = False
    game_exp: Dict[GameTypes, int] = field(default_factory=dict)
    # harder to get data from
    # game_exp: List[Tuple(GameType, int)] = field(default_factory=list)

    def __post_init__(self):
        self.created = utils.convert_to_datetime(self.created)
        self.tag_color = utils.get_color_type(self.tag_color)
        self.level = utils.get_guild_level(self.exp)

        self.preferred_games = [
            utils.get_game_type(game)
            for game in self.preferred_games
        ]
        self.ranks = [
            GuildRank(**utils._clean(rank, 'GUILD_RANK'))
            for rank in self.ranks
        ]
        self.members = [
            GuildMember(**utils._clean(member, 'GUILD_MEMBER', extra=self.ranks))
            for member in self.members
        ]
