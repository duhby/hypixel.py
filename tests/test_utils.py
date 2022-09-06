"""Tests for hypixel.utils"""

# from contextlib import nullcontext as does_not_raise
import pytest

from hypixel import utils


@pytest.mark.parametrize(
    ('number', 'expected'),
    [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
    ],
)
def test_romanize(number, expected):
    assert utils.romanize(number) == expected


@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    [
        (1, 1, 1.0),
        (1, 0, 1.0),
        (0, 1, 0.0),
    ],
)
def test_safe_div(a, b, expected):
    result = utils.safe_div(a, b)
    assert result == expected
    assert isinstance(result, type(expected))




# @pytest.mark.parametrize(
#     ('inputs', 'expectation'),
#     [
#         ((1, 1), does_not_raise()),
#         ((1, 0), does_not_raise()),
#     ]
# )
# def test_safe_div(inputs, expectation):
#     with expectation:
#         assert utils.safe_div(*inputs) is not None