"""
The MIT License (MIT)

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

from dataclasses import dataclass

from datetime import datetime
from typing import Optional
from typing import List
from typing import Dict
from typing import Any
from aiohttp import ClientResponse

from .. import utils

from .games import *
from . import Socials
from . import Achievement
from . import Game
from . import Parkour

from . import Bedwars

__all__ = (
    Player,
)

@dataclass
class Player:
    """Base model for player stats.

    Attributes
    ----------
    raw: Dict[str, Any]
        The raw json response data.
    response: ClientResponse
        The raw response object returned from the API.
    id: str
        The Hypixel ID of the player.
    uuid: str
        The Mojang UUID of the player.
    first_login: datetime
        The first login time of the player.
    name: str
        The Minecraft username of the player.

        .. note::

            This won't always be up to date with Mojang's servers, as it
            only updates when the player logs on Hypixel.
    last_login: datetime
        The last login time of the player.
    last_logout: datetime
        The last logout time of the player.
    known_aliases: List[str]
        A list of known past usernames.
    achievements: List[Achievement]
        A list of current achievements the player has.
    achievement_points: int:
        The currnet amount of achievement points the player has.
    network_exp: int
        The current amount of network experience the player has.
    karma: int
        The current amount of karma the player has.
    version: Optional[str]
        The last Minecraft version the player logged in using.

        .. warning::

            Sometimes returns ``None`` due to the fact that players
            could have logged into the server with an unrecognized
            server protocol at the time which doesn't want to fix
            itself afterwards deeming this value as unstable.
    current_gadget: Optional[str]
        The current gadget the player has equipped.
    channel: Optional[str]
        The current channel the player is in.
    most_recent_game: Optional[Game]
        The most recent game type of the player.
    level: float
        The current network level of the player. Up to 2 decimal places.
    socials: Socials
        A :class:`Socials` object of the player's linked social accounts.
    parkour: Parkour
        A :class:`Parkour` object of the player's parkour times.
    bedwars: Bedwars
        A :class:`Bedwars` object of the player's bedwars stats.
    """
    raw: Dict[str, Any]
    response: ClientResponse
    id: str
    uuid: str
    first_login: datetime
    name: str
    last_login: datetime
    last_logout: datetime
    known_aliases: List[str]
    achievements: List[Achievement] # should always exist because of 'general_first_join'
    achievement_points: int
    network_exp: int
    karma: int
    version: str = None
    current_gadget: str = None
    channel: str = None
    most_recent_game: Game = None

    def __post_init__(self):
        player_data = self.raw['player']
        stats = player_data.get('stats')
        if stats:
            if stats.get('Bedwars'):
                input_data = utils._clean(stats['bedwars'], 'bedwars')
                input_data['_raw'] = self.raw
                self.bedwars = Bedwars(**input_data)

        # level
        self.level: float = utils.get_level(self.network_exp)

        # socials
        socials = utils._clean(self._data, mode='socials')
        self.socials: Socials = Socials(**socials)

        # parkour
        parkour = utils._clean(self._data, mode='parkour')
        self.parkour: Parkour = Parkour(**parkour)
