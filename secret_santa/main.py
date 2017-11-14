from secret_santa.input import get_names_list_from_input
from secret_santa.logic import generate_secret_santa_matches


def run_secret_santa():
    names_list = get_names_list_from_input()
    secret_santa_matches = generate_secret_santa_matches(names_list)
    print(secret_santa_matches)


if __name__ == '__main__':
    run_secret_santa()
