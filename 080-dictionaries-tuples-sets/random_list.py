#!/usr/bin/env python3


def generate_random_number_list(length_of_list_to_generate):
    from random import randint

    random_list = set()

    while len(random_list) < length_of_list_to_generate:
        random_list.add(randint(1, 100))

    return list(random_list)


if __name__ == "__main__":
    print(generate_random_number_list(10))
    print(generate_random_number_list(20))
