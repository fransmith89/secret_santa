from secret_santa.error import InputError


def get_names_list_from_input():
    user_message = (
        'To get your Secret Santa list, enter the names of everyone participating.'
        '\n(Note: You will need at least 2 names and each name must be separated by a comma):\n'
    )
    while user_message is not None:
        names = input(user_message)
        # strip any extra space because ' bill' looks odd
        names_list = [name.strip() for name in names.split(',')]
        try:
            validate_input(names_list)
            return names_list
        except InputError as err:
            user_message = err.message


def validate_input(names_list):
    if len(names_list) < 2:
        raise InputError(
            'You need to enter at least 2 names, with each name separated by a comma,'
            ' for a secret santa list to be generated\n:'
        )
    elif '' in names_list or ' ' in names_list:
        raise InputError(
            'You entered empty spaces. You need to enter at least 2 names, with each'
            ' name separated by a comma, for a secret santa list to be generated\n:'
        )
    elif len(names_list) > len(set(names_list)):
        # This ignores case so Sarah and sarah won't error but they are distinguishable
        raise InputError(
            'There are some duplicate names, add in a surname or some other way to identify them.'
            'Remember You need to enter at least 2 names, with each name separated by a comma,'
            ' for a secret santa list to be generated\n:'
        )
    return None
