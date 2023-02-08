"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal, List, Optional

from ...achievement import Achievement
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

    .. tip::

        You can use the ``==`` operator to compare two
        :class:`~hypixel.models.player.Player` classes.

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
        The username of the player with correct capitalization.

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

        .. tip::

            You can use :meth:`hypixel.Achievement.from_type` to get
            the achievement object from a name string.
    network_exp: :class:`int`
        The player's current network experience points.
    karma: :class:`int`
        The player's current karma.
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

        Possible values are ``'VIP'``, ``'VIP+'``, ``'MVP'``,
        ``'MVP+'``, ``'MVP++'``, ``'YOUTUBE'``, ``'PIG+++'``,
        ``'MOJANG'``, ``'GAME MASTER'``, ``'ADMIN'``, and ``'OWNER'``.
    plus_color: Optional[:class:`~hypixel.Color`]
        The player's plus color if their rank has a plus in it;
        otherwise ``None``.
    level: :class:`float`
        The player's Hypixel level.
    most_recent_game: Optional[:class:`~hypixel.Game`]
        The player's most recent game they played.

        .. note::

            Will be ``None`` if the player's ``Recent Games`` API
            setting is disabled.
    arcade: :class:`~hypixel.models.player.Arcade`
        A model for abstracting arcade data.
    bedwars: :class:`~hypixel.models.player.Bedwars`
        A model for abstracting bedwars data.
    blitz: :class:`~hypixel.models.player.Blitz`
        A model for abstracting blitz data.
    duels: :class:`~hypixel.models.player.Duels`
        A model for abstracting duels data.
    murder_mystery: :class:`~hypixel.models.player.MurderMystery`
        A model for abstracting murder mystery data.
    paintball: :class:`~hypixel.models.player.Paintball`
        A model for abstracting paintball data.
    parkour: :class:`~hypixel.models.player.Parkour`
        A model for abstracting parkour data.
    skywars: :class:`~hypixel.models.player.Skywars`
        A model for abstracting skywars data.
    socials: :class:`~hypixel.models.player.Socials`
        A model for abstracting socials data.
    tkr: :class:`~hypixel.models.player.TurboKartRacers`
        A model for abstracting tkr data.
    tnt_games: :class:`~hypixel.models.player.TntGames`
        A model for abstracting tnt games data.
    uhc: :class:`~hypixel.models.player.Uhc`
        A model for abstracting uhc data.
    wool_games: :class:`~hypixel.models.player.WoolGames`
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

        # Some achievement items can be blank, non-string objects.
        for achievement in self.achievements:
            if not isinstance(achievement, str):
                self.achievements.remove(achievement)

        self.level = utils.get_network_level(self.network_exp)
        self.rank = utils.get_rank(self.raw)
        self.most_recent_game = Game.from_type(
            self.raw.get('player', {}).get('mostRecentGameType')
        )
        self.plus_color = Color.from_type(self._data.get('rankPlusColor'))

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

    def build_achievements(self):
        """Converts the achievements in :attr:`achievements` to
        List[:class:`~hypixel.Achievement`].

        .. warning::

            If the package ``hypixel.py-data`` is not installed, this
            will convert :attr:`achievements` to a list of ``None``
            types.
        """
        built_achievements = []
        for achievement in self.achievements:
            achievement = Achievement.from_type(achievement)
            if achievement:
                built_achievements.append(achievement)
        self.achievements = built_achievements

    def __eq__(self, other: object):
        if isinstance(other, Player):
            return self.uuid == other.uuid
        return False
