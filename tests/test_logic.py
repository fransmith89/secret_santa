from unittest.mock import patch

from secret_santa.logic import generate_secret_santa_matches, get_secret_santa_name
from secret_santa.logic import swap_first_secret_santa_name


def test_generate_secret_santa_matches_returns_dictionary():
    names_list = ['bill', 'bob']

    res = generate_secret_santa_matches(names_list)

    assert(type(res) == dict)


def test_generate_secret_santa_assigns_everyone_a_different_name():
    names_list = ['bill', 'bob']

    res = generate_secret_santa_matches(names_list)

    assert(res['bill'] == 'bob')
    assert(res['bob'] == 'bill')


def test_swap_first_secret_santa_name_swaps_name_with_first_in_list():
    secret_santa_matches = {'bill': 'bob', 'bob': 'bill'}
    names_list = ['bill', 'bob', 'ben']
    name = 'ben'

    swap_first_secret_santa_name(name, names_list, secret_santa_matches)

    assert({'bill': 'ben', 'bob': 'bill', 'ben': 'bob'} == secret_santa_matches)


@patch('random.choice')
def test_get_secret_santa_name_ignores_current_name_when_choosing(random_choice_mock):
    name = 'bill'
    remaining_names = ['bill', 'bob']

    get_secret_santa_name(name, remaining_names)

    random_choice_mock.assert_called_with(['bob'])
