from ..player_actions.command_parser import CommandParser
import pytest

@pytest.mark.parametrize("user_input,expected_command,expected_arguments",[
    ("attack troll", "attack", {"target": "troll", "weapons": []}),
    ("attack the troll", "attack", {"target": "troll", "weapons": []}),
    ("attack the troll with a sword", "attack", {"target": "troll", "weapons": ["sword"]}),
    ("attack the troll with a sword and hammer", "attack", {"target": "troll", "weapons": ["sword", "hammer"]}),
])
def test_get_command_and_arguments_from_input_returns_correct_values(user_input,expected_command,expected_arguments):
    parser = CommandParser()

    output_command, output_arguments = parser.get_command_and_arguments_from_input(user_input)
    
    assert expected_command == output_command
    assert expected_arguments == output_arguments


@pytest.mark.parametrize("user_input,expected_arguments",[
    ("attack the troll with a sword and hammer and a spear", {"target": "troll", "weapons": ["hammer", "spear"]}),
])
def test_get_command_and_arguments_from_input_does_not_return_more_than_two_weapons(user_input,expected_arguments):
    parser = CommandParser()

    output_command, output_arguments = parser.get_command_and_arguments_from_input(user_input)
    
    assert expected_arguments == output_arguments


#def test_check_first_word_gets_a_command():