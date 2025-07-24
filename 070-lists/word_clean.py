#!/usr/bin/env python3


def clean_string(s):
    return "".join([c for c in s if c.isalpha()])


if __name__ == "__main__":
    for test_string in ["abcde", "a***bcd((e))", "&&&&", "A123"]:
        print(f"'{test_string}' -> '{clean_string(test_string)}'")
