"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal, List, Optional

from ...color import Color
from ...game import Game

from .arcade import Arcade
from .bedwars import Bedwars
from .blitz import Blitz
from .duels import Duels
from .murder_mystery import MurderMystery
from .paintball import Paintball
from .parkour import Parkour
from .skywars import Skywars
from .socials import Socials
from .tkr import TurboKartRacers
from .tnt_games import TntGames
from .uhc import Uhc
from .wool_games import WoolGames

from . import utils

__all__ = [
    'Player',
]


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
        The first login time represented as a datetime in the UTC
        timezone.
    name: :class:`str`
        The username of the player with the correct capitalization.

        .. note::

            If the player changed their username after ``last_login``,
            then this attribute will be outdated.
    last_login: :class:`datetime.datetime`
        The last login time represented as a datetime in the UTC
        timezone.
    last_logout: :class:`datetime.datetime`
        The last logout time represented as a datetime in the UTC
        timezone.
    known_aliases: List[:class:`str`]
        A list of previous usernames the account has logged onto Hypixel
        with.
    achievements: List[:class:`str`]
        A list of achievement name strings.

        .. warning::

            This will most likely be changed to List[Achievement] before
            the 1.0 release.
    network_exp: :class:`int`
        The player's current network experience points.
    karma: :class:`int`
        The player's current karma.
    version: :class:`str`
        The most recent minecraft version the player joined Hypixel
        with.

        .. note::

            This attribute is highly unstable, and the API often returns
            inaccurate info or nothing at all.

        .. deprecated:: 1.0

            It seems as though Hypixel has deprecated this already.
    achievement_points: :class:`int`
        The player's achievement points.
    current_gadget: :class:`str`
        The player's current gadget equipped in lobbies.
    channel: Optional[:class:`str`]
        The current text channel the player is in.

        .. note::

            Will be ``None`` if the player's ``Online Status`` API
            setting is disabled.
    rank: Optional[:class:`str`]
        A string representation of the player's rank if it exists;
        otherwise ``None``.

        Possible values are 'VIP', 'VIP+', 'MVP', 'MVP+', 'MVP++',
        'YOUTUBE', 'PIG+++', 'MOJANG', 'GAME MASTER', 'ADMIN', and
        'OWNER'.
    plus_color: Optional[:class:`~hypixel.Color`]
        The player's plus color if their rank has a plus in it;
        otherwise ``None``.
    level: :class:`float`
        The player's Hypixel level.
    most_recent_game: Optional[:class:`~hypixel.Game`]
        .. note::

            Will be ``None`` if the player's ``Recent Games`` API
            setting is disabled.
    arcade: :class:`~models.playerdata.Arcade`
        A model for abstracting arcade data.
    bedwars: :class:`~models.playerdata.Bedwars`
        A model for abstracting bedwars data.
    blitz: :class:`~models.playerdata.Blitz`
        A model for abstracting blitz data.
    duels: :class:`~models.playerdata.Duels`
        A model for abstracting duels data.
    murder_mystery: :class:`~models.playerdata.MurderMystery`
        A model for abstracting murder mystery data.
    paintball: :class:`~models.playerdata.Paintball`
        A model for abstracting paintball data.
    parkour: :class:`~models.playerdata.Parkour`
        A model for abstracting parkour data.
    skywars: :class:`~models.playerdata.Skywars`
        A model for abstracting skywars data.
    socials: :class:`~models.playerdata.Socials`
        A model for abstracting socials data.
    tkr: :class:`~models.playerdata.TurboKartRacers`
        A model for abstracting tkr data.
    tnt_games: :class:`~models.playerdata.TntGames`
        A model for abstracting tnt games data.
    uhc: :class:`~models.playerdata.Uhc`
        A model for abstracting uhc data.
    wool_games: :class:`~models.playerdata.WoolGames`
        A model for abstracting wool games data.
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
    rank: Optional[str] = field(init=False)
    plus_color: Optional[Color] = field(init=False)
    level: float = field(init=False)
    most_recent_game: Optional[Game] = field(init=False)
    arcade: Arcade = field(init=False)
    bedwars: Bedwars = field(init=False)
    blitz: Blitz = field(init=False)
    duels: Duels = field(init=False)
    murder_mystery: MurderMystery = field(init=False)
    paintball: Paintball = field(init=False)
    parkour: Parkour = field(init=False)
    skywars: Skywars = field(init=False)
    socials: Socials = field(init=False)
    tkr: TurboKartRacers = field(init=False)
    tnt_games: TntGames = field(init=False)
    uhc: Uhc = field(init=False)
    wool_games: WoolGames = field(init=False)

    def __post_init__(self):
        for date in ('first_login', 'last_login', 'last_logout'):
            value = getattr(self, date)
            if value is None:
                continue
            dt = utils.convert_to_datetime(value)
            setattr(self, date, dt)
        self.network_exp = int(self.network_exp)

        self.level = utils.get_network_level(self.network_exp)
        self.rank = utils.get_rank(self.raw)
        self.most_recent_game = Game.from_type(
            self.raw.get('player', {}).get('mostRecentGameType')
        )
        self.plus_color = Color.from_type(self._data.get('rankPlusColor'))

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
            'tnt_games': TntGames,
            'uhc': Uhc,
            'wool_games': WoolGames,
        }
        for mode, model in modes.items():
            data = utils._clean(self._data, mode=mode.upper())
            setattr(self, mode, model(**data))

    def __eq__(self, other: object):
        if isinstance(other, Player):
            return self.uuid == other.uuid
        return False
