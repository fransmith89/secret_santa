def get_names_list_from_input():
    user_message = (
        "To get your Secret Santa list, enter the names of everyone participating."
        "\n(Note: You will need at least 2 names and each name must be separated by a comma):\n"
    )
    names = input(user_message)
    names_list = [name.strip() for name in names.split(',')]
    return names_list