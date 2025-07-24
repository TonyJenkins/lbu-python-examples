#!/usr/bin/env python3


def generate_random_number_list(length_of_list_to_generate):
    from random import randint

    random_list = set()

    while len(random_list) < length_of_list_to_generate:
        random_list.add(randint(1, 100))

    return list(random_list)


def get_unique_scores():
    scores = set()

    while True:
        try:
            scores.add(int(input("Enter a score: ")))
        except (
            TypeError,
            ValueError,
        ):
            break

    return list(scores)


if __name__ == "__main__":
    print(
        f"Your unique scores are: {', '.join([str(num) for num in get_unique_scores()])}"
    )
