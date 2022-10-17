"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

from ..color import Color
from ..game import Game

from . import utils

__all__ = [
    'Guild',
    'GuildMember',
    'GuildRank',
]


@dataclass
class GuildRank:
    name: str
    default: bool = False # Unstable: some guilds don't have a default
    created: Optional[datetime] = None
    priority: Optional[int] = None
    tag: Optional[str] = None

    def __post_init__(self):
        if self.created is not None:
            self.created = utils.convert_to_datetime(self.created)

    def __gt__(self, other):
        if isinstance(other, GuildRank):
            if self.priority is not None and other.priority is not None:
                return self.priority > other.priority

    def __lt__(self, other):
        if isinstance(other, GuildRank):
            if self.priority is not None and other.priority is not None:
                return self.priority < other.priority

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
            datetime.fromisoformat(time).replace(tzinfo=timezone.utc): value
            for time, value in self.exp_history.items()
        }

@dataclass
class Guild:
    """Guild model object."""
    # raw: dict = field(repr=False) # Currently has bug
    id: str
    name: str
    exp: int
    created: datetime
    level: int = field(init=False)
    legacy_rank: Optional[int] = None
    members: List[GuildMember] = field(default_factory=list)
    ranks: List[GuildRank] = field(default_factory=list)
    winners: int = 0
    experience_kings: int = 0
    most_online_players: int = 0
    joinable: bool = False
    tag: Optional[str] = None
    tag_color: Optional[Color] = None
    description: Optional[str] = None
    preferred_games: List[Game] = field(default_factory=list)
    publicly_listed: bool = False
    game_exp: List[Tuple(Game, int)] = field(default_factory=list)

    def __post_init__(self):
        self.created = utils.convert_to_datetime(self.created)
        self.tag_color = Color.from_type(self.tag_color)
        self.level = utils.guild_level(self.exp)

        self.preferred_games = [
            Game.from_type(game)
            for game in self.preferred_games
        ]
        self.game_exp = [
            (Game.from_type(game), x)
            for game, x in self.game_exp.items()
        ]
        self.ranks = [
            GuildRank(**utils._clean(rank, 'GUILD_RANK'))
            for rank in self.ranks
        ]
        self.members = [
            GuildMember(**utils._clean(member, 'GUILD_MEMBER', extra=self.ranks))
            for member in self.members
        ]
