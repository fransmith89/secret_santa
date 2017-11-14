from unittest.mock import patch

from secret_santa.input import get_names_list_from_input


@patch('builtins.input')
def test_get_names_list_from_input_returns_a_list(input_mock):
    input_mock.return_value = 'bill, ben'

    res = get_names_list_from_input()

    assert(type(res) == list)


@patch('builtins.input')
def test_get_names_list_from_input_returns_2_items_when_2_names_given_with_comma(input_mock):
    input_mock.return_value = 'bill, ben'

    res = get_names_list_from_input()

    assert(len(res) == 2)


@patch('builtins.input')
def test_get_names_list_from_input_returns_1_items_when_2_names_given_with_no_comma(input_mock):
    input_mock.return_value = 'bill ben'

    res = get_names_list_from_input()

    assert(len(res) == 1)


@patch('builtins.input')
def test_get_names_list_from_input_returns_strips_white_space_from_name(input_mock):
    input_mock.return_value = 'bill, ben'

    res = get_names_list_from_input()

    assert(res[1] == 'ben')
