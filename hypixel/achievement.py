"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from __future__ import annotations
from dataclasses import dataclass
import functools
from typing import Optional

from . import utils

try:
    import hypixel_data
    ACHIEVEMENTS = hypixel_data.achievements.data['achievements']
except ImportError:
    hypixel_data = None

__all__ = [
    'Achievement',
]


@dataclass
class Achievement:
    """Represents a Hypixel achievement.

    Attributes
    ----------
    type_name: :class:`str`
        The type name used to reference the achievement in the Hypixel
        API.
    points: :class:`int`
        Amount of achievement points the achievement is worth.
    name: :class:`str`
        The name of the achievement.
    description: :class:`str`
        The description of the achievement.
    global_unlocked: Optional[:class:`float`]
        The percentage of players who have unlocked the achievement.

        .. note::

            For achievements which :attr:`legacy` is ``True``, this
            attribute will be ``None``.
    game_unlocked: Optional[:class:`float`]
        The percentage of players who have unlocked the achievement
        that have played the game.

        .. note::

            Achievements that do not have a game associated with them
            will have this attribute as ``None``.
    legacy: :class:`bool`
        Whether or not the achievement is legacy.
    """
    type_name: str
    points: int
    name: str
    description: str
    global_unlocked: Optional[float] = None
    game_unlocked: Optional[float] = None
    legacy: bool = False

    @classmethod
    @functools.lru_cache()
    def from_type(cls, type_name: str) -> Optional[Achievement]:
        """Constructs a :class:`Achievement` from its type name.

        .. warning::

            Some achievements that come from the Hypixel API will return
            ``None``. This is because the API does not provide the data
            for some older achievements.

        .. warning::

            If the module ``hypixel.py-data`` is not installed, this
            method will always return ``None``.

        Parameters
        ----------
        type_name: :class:`str`
            The type name used in Hypixel API attributes.

        Returns
        -------
        Optional[:class:`Achievement`]
            The constructed achievement, or ``None`` if the achievement
            could not be found.
        """
        if not hypixel_data:
            return None
        category = type_name.split('_')[0]
        if category == 'bridge':
            category = 'duels'
        name = type_name.split('_')[1:]
        # Some achievement names are not all uppercase.
        name = '_'.join(name).lower()
        data = ACHIEVEMENTS.get(category, {}).get('one_time', {})
        # Some achievements are not all uppercase.
        data = {k.lower(): v for k, v in data.items()}
        data = data.get(name)
        if not data:
            return None
        data['type_name'] = type_name
        return cls(**utils._clean(data, 'ACHIEVEMENT'))
