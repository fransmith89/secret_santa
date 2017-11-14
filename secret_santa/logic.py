import random


def generate_secret_santa_matches(names_list):
    secret_santa_matches = {}
    remaining_names = names_list[:]
    for name in names_list:
        # We could end up with the last person getting themselves (which doesn't seem very fun)
        # so let's swap their Secret Santa name with the first person we matched.
        if len(remaining_names) == 1 and name in remaining_names:
            swap_first_secret_santa_name(name, names_list, secret_santa_matches)
        else:
            secret_santa_name = get_secret_santa_name(name, remaining_names)
            secret_santa_matches[name] = secret_santa_name
            remaining_names.remove(secret_santa_name)
    return secret_santa_matches


def swap_first_secret_santa_name(name, names_list, secret_santa_matches):
    first_secret_santa_name = names_list[0]
    secret_santa_matches[name] = secret_santa_matches[first_secret_santa_name]
    secret_santa_matches[first_secret_santa_name] = name


def get_secret_santa_name(name, remaining_names):
    remaining_names = remaining_names[:]
    if name in remaining_names:
        remaining_names.remove(name)
    return random.choice(remaining_names)
