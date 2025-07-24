#!/usr/bin/env python3

import sys

from caesar import rot_string


def replace_newlines_with_spaces(s):
    s.replace("\n", " ")
    return s


def remove_punctuation(s):
    return "".join([c for c in s if c.isalpha() or c.isspace()])


def check_for_the_common_words(s, rotation_to_try):
    common_words = [
        "the",
        "be",
        "to",
        "of",
        "and",
        "a",
        "in",
        "that",
        "have",
    ]

    s = s.lower()
    s = replace_newlines_with_spaces(s)
    s = remove_punctuation(s)
    s = rot_string(s, -rotation_to_try)

    word_count = 0

    for word in s.split():
        if word in common_words:
            word_count += 1

        if word_count > 2:
            return True

    return False


def crack_the_code(rotted_file):
    with open(rotted_file, "r") as rf:
        rotated_contents = rf.read()

        for possible_rotation in range(1, 26):
            if check_for_the_common_words(rotated_contents, possible_rotation):
                print(rot_string(rotated_contents, -possible_rotation))
                break


if __name__ == "__main__":
    try:
        crack_the_code(sys.argv[1])
    except (IndexError, FileNotFoundError,):
        print(f"Usage: {sys.argv[0]} <file to crack>")
