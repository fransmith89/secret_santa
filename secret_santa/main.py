from secret_santa.input import get_names_list_from_input


def run_secret_santa():
    names = get_names_list_from_input()
    print(names)


if __name__ == '__main__':
    run_secret_santa()
