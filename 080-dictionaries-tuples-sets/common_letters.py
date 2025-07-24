#!/usr/bin/env python3


def common_letters(string_one, string_two):
    return "".join(set(string_one) & set(string_two))


if __name__ == "__main__":
    for test_pair in [
        (
            "eggs",
            "cheese",
        ),
        (
            "cheese",
            "cheese",
        ),
        (
            "sausage",
            "bacon",
        ),
        (
            "sausage",
            "",
        ),
    ]:
        first, second = test_pair
        print(f"{test_pair} -> {common_letters(first, second)}")
