#!/usr/bin/env python3


def reverse_string(s):
    return s[::-1]


if __name__ == "__main__":

    for test_string in ["cheese", "spam", "edam", "elderberries", "", "abcdef"]:
        print(f"{test_string} -> {reverse_string(test_string)}")
