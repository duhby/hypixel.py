"""
Copyright (c) 2021-present duhby
MIT License, see LICENSE for more details.
"""

from __future__ import annotations
from dataclasses import dataclass
import functools

__all__ = [
    'Color',
]


@dataclass
class Color:
    """Represents a Minecraft color.

    Attributes
    ----------
    type_name: :class:`str`
        The name used to reference the color in the Hypixel API.
    clean_name: :class:`str`
        The color name in Title Case.
    chat_code: :class:`str`
        The Minecraft chat formatting code for the color.
    hexadecimal: :class:`str`
        The hexadecimal value of the color.
    """
    type_name: str
    clean_name: str
    chat_code: str
    hexadecimal: str

    @classmethod
    @functools.lru_cache()
    def from_type(cls, type_name: str) -> Color:
        """Constructs a :class:`Color` from its type name.

        Parameters
        ----------
        type_name: :class:`str`
            The type name used in Hypixel API attributes.
        """
        data = next((
            item for item in COLOR_TYPES if item['type_name'] == type_name
        ), None)
        if not data:
            return None
        return cls(**data)

COLOR_TYPES = [
    {
        'type_name': 'DARK_RED',
        'clean_name': 'Dark Red',
        'chat_code': '§4',
        'hexadecimal': 'AA0000',
    },
    {
        'type_name': 'RED',
        'clean_name': 'Red',
        'chat_code': '§c',
        'hexadecimal': 'FF5555',
    },
    {
        'type_name': 'GOLD',
        'clean_name': 'Gold',
        'chat_code': '§6',
        'hexadecimal': 'FFAA00',
    },
    {
        'type_name': 'YELLOW',
        'clean_name': 'Yellow',
        'chat_code': '§e',
        'hexadecimal': 'FFFF55',
    },
    {
        'type_name': 'DARK_GREEN',
        'clean_name': 'Dark Green',
        'chat_code': '§2',
        'hexadecimal': '00AA00',
    },
    {
        'type_name': 'GREEN',
        'clean_name': 'Green',
        'chat_code': '§a',
        'hexadecimal': '55FF55',
    },
    {
        'type_name': 'AQUA',
        'clean_name': 'Aqua',
        'chat_code': '§b',
        'hexadecimal': '55FFFF',
    },
    {
        'type_name': 'DARK_AQUA',
        'clean_name': 'Dark Aqua',
        'chat_code': '§3',
        'hexadecimal': '00AAAA',
    },
    {
        'type_name': 'DARK_BLUE',
        'clean_name': 'Dark Blue',
        'chat_code': '§1',
        'hexadecimal': '0000AA',
    },
    {
        'type_name': 'BLUE',
        'clean_name': 'Blue',
        'chat_code': '§9',
        'hexadecimal': '5555FF',
    },
    {
        'type_name': 'LIGHT_PURPLE',
        'clean_name': 'Light Purple',
        'chat_code': '§d',
        'hexadecimal': 'FF55FF',
    },
    {
        'type_name': 'DARK_PURPLE',
        'clean_name': 'Dark Purple',
        'chat_code': '§5',
        'hexadecimal': 'AA00AA',
    },
    {
        'type_name': 'WHITE',
        'clean_name': 'White',
        'chat_code': '§f',
        'hexadecimal': 'FFFFFF',
    },
    {
        'type_name': 'GRAY',
        'clean_name': 'Gray',
        'chat_code': '§7',
        'hexadecimal': 'AAAAAA',
    },
    {
        'type_name': 'DARK_GRAY',
        'clean_name': 'Dark Gray',
        'chat_code': '§8',
        'hexadecimal': '555555',
    },
    {
        'type_name': 'BLACK',
        'clean_name': 'Black',
        'chat_code': '§0',
        'hexadecimal': '000000',
    },
]
