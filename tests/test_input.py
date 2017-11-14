from unittest.mock import patch

import pytest

from secret_santa.error import InputError
from secret_santa.input import get_names_list_from_input, validate_input


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
def test_get_names_list_from_input_strips_white_space_from_name(input_mock):
    input_mock.return_value = 'bill, ben '

    res = get_names_list_from_input()

    assert(res[1] == 'ben')


@patch('builtins.input')
def test_get_names_list_from_input_only_returns_valid_data(input_mock):
    # A couple of invalid entries followed by a valid one
    input_mock.side_effect = ['bill ben', 'bill, ', 'bill, ben']

    res = get_names_list_from_input()

    assert(res == ['bill' , 'ben'])


def test_validate_input_returns_none_when_valid_list_given():
    names_list = ['bill', 'ben']

    res = validate_input(names_list)

    assert(res == None)


@pytest.mark.parametrize('names_list', [['bill'], []])
def test_validate_input_raises_error_when_less_than_2_names_given(names_list):
    with pytest.raises(InputError):
        validate_input(names_list)


@pytest.mark.parametrize('names_list', [['bill', '', 'ben'], [' ', 'bill']])
def test_validate_input_raises_error_when_empty_names_in_list(names_list):
    with pytest.raises(InputError):
        validate_input(names_list)


def test_validate_input_raises_error_when_duplicate_names_in_list():
    names_list = ['bill', 'ben', 'bill']

    with pytest.raises(InputError):
        validate_input(names_list)
