#!/usr/bin/env python3

import sys

from caesar import rot_string


def find_most_common_letter(s):
    from collections import Counter

    letters = "".join([c for c in s if c.isalpha()])
    counter = Counter(letters)

    return max(counter, key=counter.get)


def crack_the_code(rotted_file):
    from string import ascii_lowercase as letters

    with open(rotted_file, "r") as rf:
        rotated_contents = rf.read()
        most_common_letter = find_most_common_letter(rotated_contents.lower())

        probable_rotation = letters.index(most_common_letter) - letters.index("e")

        print(rot_string(rotated_contents, -probable_rotation))


if __name__ == "__main__":
    try:
        crack_the_code(sys.argv[1])
    except (IndexError, FileNotFoundError,):
        print(f"Usage: {sys.argv[0]} <file to crack>")
