from hypixel import Achievement
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


@pytest.mark.parametrize(
    ('type_name', 'expected'),
    [
        ('murdermystery_be_the_hero', Achievement),
        ('invalid_achievement_thing', type(None)),
    ]
)
def test_achievement_from_type(type_name, expected):
    achievement = Achievement.from_type(type_name)
    assert type(achievement) is expected


def test_achievement():
    achievement = Achievement.from_type('murdermystery_be_the_hero')
    assert achievement.type_name == 'murdermystery_be_the_hero'
    assert achievement.points == 5
    assert achievement.name == 'Saving The Day'
    assert achievement.description == 'Be the hero of the game'
    assert achievement.global_unlocked == 17.068763596482807
    assert achievement.game_unlocked == 49.597447693931095
    assert achievement.legacy == False


def test_achievement_legacy():
    achievement = Achievement.from_type('general_treasure_hunt')
    assert achievement.type_name == 'general_treasure_hunt'
    assert achievement.points == 0
    assert achievement.name == 'Treasure Hunt 2020'
    assert achievement.description == 'Complete the 2020 Hypixel Anniversary Quest. Thank you for being a part of Hypixel!'
    assert achievement.global_unlocked == None
    assert achievement.game_unlocked == None
    assert achievement.legacy == True
