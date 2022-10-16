from hypixel import Color
from hypixel import Game
import pytest


@pytest.mark.parametrize(
    ('type_name', 'expected'),
    [
        ('DARK_RED', Color),
        ('INVALID_NAME', type(None)),
    ]
)
def test_color_from_type(type_name, expected):
    color = Color.from_type(type_name)
    assert type(color) is expected


def test_color():
    color = Color.from_type('DARK_RED')
    assert color.type_name == 'DARK_RED'
    assert color.clean_name == 'Dark Red'
    assert color.chat_code == '§4'
    assert color.hexadecimal == 'AA0000'


@pytest.mark.parametrize(
    ('type_name', 'expected'),
    [
        ('BEDWARS', Game),
        ('INVALID_NAME', type(None)),
    ]
)
def test_game_from_type(type_name, expected):
    game = Game.from_type(type_name)
    assert type(game) is expected


@pytest.mark.parametrize(
    ('id_', 'expected'),
    [
        (2, Game),
        (1, type(None)),
    ]
)
def test_game_from_id(id_, expected):
    game = Game.from_id(id_)
    assert type(game) is expected


def test_game():
    game = Game.from_type('BEDWARS')
    assert game.id == 58
    assert game.type_name == 'BEDWARS'
    assert game.database_name == 'Bedwars'
    assert game.clean_name == 'Bed Wars'
    assert game.standard_name == 'Bed Wars'
