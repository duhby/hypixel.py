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

from dataclasses import dataclass, fields, field
from datetime import datetime

from typing import List, Literal, Optional
from .types import ColorType, GameType
from ..constants import RankTypes

from .. import utils

from .playerdata import Arcade
from .playerdata import Bedwars
from .playerdata import Blitz
from .playerdata import Duels
from .playerdata import MurderMystery
from .playerdata import Paintball
from .playerdata import Parkour
from .playerdata import Skywars
from .playerdata import Socials
from .playerdata import TurboKartRacers
from .playerdata import Uhc

__all__ = (
    'Player',
)

@dataclass
class Player:
    """Player model object.

    Attributes
    ----------
    raw: :class:`dict`
        The raw json response returned from the API.
    id: :class:`str`
        Hypixel's unique identifier.
    uuid: :class:`str`
        Mojang's unique identifier.
    first_login: :class:`datetime.datetime`
        The first login time represented as a datetime in the UTC timezone.
    name: :class:`str`
        The username of the player with the correct capitalization.

        .. note::

            If the player changed their username after ``last_login``, then this attribute
            will be outdated.
    last_login: :class:`datetime.datetime`
        The last login time represented as a datetime in the UTC timezone.
    last_logout: :class:`datetime.datetime`
        The last logout time represented as a datetime in the UTC timezone.
    known_aliases: List[:class:`str`]
        A list of previous usernames the account has logged onto Hypixel with.
    achievements: List[:class:`str`]
        A list of achievement name strings.

        .. warning::

            This will most likely be changed to List[Achievement] before the 1.0 release.
    network_exp: :class:`int`
        The player's current network experience points.
    karma: :class:`int`
        The player's current karma.
    version: :class:`str`
        The most recent minecraft version the player joined Hypixel with.

        .. note::

            This attribute is highly unstable, and the API often returns inaccurate info
            or nothing at all.
    achievement_points: :class:`int`
        The player's achievement points.
    current_gadget: :class:`str`
        The player's current gadget equipped in lobbies.
    channel: Optional[:class:`str`]
        The current text channel the player is in.

        .. note::

            Will be ``None`` if the player's ``Online Status`` API setting is disabled.
    rank: Optional[:class:`RankTypes`]
        A string representation of the player's rank if it exists; otherwise ``None``.
    plus_color: Optional[:class:`ColorType`]
        The player's plus color if their rank has a plus in it; otherwise ``None``.
    level: :class:`float`
        The player's Hypixel level.
    most_recent_game: Optional[:class:`GameType`]
        .. note::

            Will be ``None`` if the player's ``Recent Games`` API setting is disabled.
    arcade: :class:`~models.playerdata.Arcade`
        A model for abstracting arcade related data.
    bedwars: :class:`~models.playerdata.Bedwars`
        A model for abstracting bedwars related data.
    duels: :class:`~models.playerdata.Duels`
        A model for abstracting duels related data.
    paintball: :class:`~models.playerdata.Paintball`
        A model for abstracting paintball related data.
    parkour: :class:`~models.playerdata.Parkour`
        A model for abstracting parkour related data.
    skywars: :class:`~models.playerdata.Skywars`
        A model for abstracting skywars related data.
    socials: :class:`~models.playerdata.Socials`
        A model for abstracting socials related data.
    tkr: :class:`~models.playerdata.TurboKartRacers`
        A model for abstracting tkr related data.
    uhc: :class:`~models.playerdata.Uhc`
        A model for abstracting uhc related data.
    """
    _data: dict = field(repr=False)
    raw: dict = field(repr=False)
    id: str = None
    uuid: str = None
    first_login: datetime = None
    name: str = None
    last_login: datetime = None
    last_logout: datetime = None
    known_aliases: list = None
    achievements: list = field(default_factory=list, repr=False)
    network_exp: int = 0
    karma: int = 0
    version: str = None
    achievement_points: int = 0
    current_gadget: str = None
    channel: str = None
    rank: Optional[RankTypes] = field(init=False)
    plus_color: Optional[ColorType] = field(init=False)
    level: float = field(init=False)
    most_recent_game: GameType = None
    arcade: Arcade = field(init=False)
    bedwars: Bedwars = field(init=False)
    duels: Duels = field(init=False)
    paintball: Paintball = field(init=False)
    parkour: Parkour = field(init=False)
    skywars: Skywars = field(init=False)
    socials: Socials = field(init=False)
    tkr: TurboKartRacers = field(init=False)
    uhc: Uhc = field(init=False)

    def __post_init__(self):
        for date in ('first_login', 'last_login', 'last_logout'):
            value = getattr(self, date)
            if value is None:
                continue
            dt = utils.convert_to_datetime(value)
            setattr(self, date, dt)
        self.network_exp = int(self.network_exp)

        self.level = utils.get_level(self.network_exp)
        self.rank = utils.get_rank(self.raw)
        self.most_recent_game = utils.get_game_type(
            self.raw.get('player', {}).get('mostRecentGameType')
        )
        self.plus_color = utils.get_color_type(self._data.get('rankPlusColor'))

        # playerdata
        modes = {
            'arcade': Arcade,
            'bedwars': Bedwars,
            'blitz': Blitz,
            'duels': Duels,
            'murder_mystery': MurderMystery,
            'paintball': Paintball,
            'parkour': Parkour,
            'skywars': Skywars,
            'socials': Socials,
            'tkr': TurboKartRacers,
            'uhc': Uhc,
        }
        for mode, model in modes.items():
            data = utils._clean(self._data, mode=mode.upper())
            setattr(self, mode, model(**data))

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.uuid == other.uuid
        return False
