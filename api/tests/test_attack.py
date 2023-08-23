from player_actions.attack import Attack
import pytest


@pytest.mark.parametrize("arguments,expected_target", [
    ({'target': 'my_test_target'}, 'my_test_target'),
    ({}, None)
])
def test_parse_returns_correct_target_value(arguments, expected_target):
    target, weapons = Attack.parse(None, arguments)

    assert expected_target == target


@pytest.mark.parametrize("arguments,expected_weapons", [
    ({'weapons': ['Sword', 'Bottle']}, ['sword', 'bottle']),
    ({}, ['fist'])
])
def test_parse_returns_correct_weapons_value(arguments, expected_weapons):
    target, weapons = Attack.parse(None, arguments)

    assert expected_weapons == weapons
