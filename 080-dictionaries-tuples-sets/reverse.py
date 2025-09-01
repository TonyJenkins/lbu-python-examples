#!/usr/bin/env python3


def reverse(s):
    return s, s[::-1]


if __name__ == "__main__":
    for test_s in [
        "spam",
        "eggs",
        "cheese",
        "gerbil",
        "moon",
    ]:
        original, reverse_original = reverse(test_s)
        print(f"{test_s} -> {original} : {reverse_original}")
