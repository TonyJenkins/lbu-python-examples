#!/usr/bin/env python3

import sys


def rot_character(c, rotation=13):
    from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase

    if not c.isalpha():
        return c

    letters = lowercase if c.islower() else uppercase

    rot13_alphabet = letters[rotation:] + letters[:rotation]

    return rot13_alphabet[letters.find(c)]


def rot_string(s, rotation=13):
    return "".join([rot_character(c, rotation) for c in s])


def rotate_a_file(filename, rotation=13):
    with open(filename, "r") as infile:
        file_contents = infile.read()

    with open(filename, "w") as rotfile:
        rotfile.write(rot_string(file_contents, rotation))


if __name__ == "__main__":
    try:
        rotate_a_file(sys.argv[1], int(sys.argv[2]))
    except (
        IndexError,
        ValueError,
    ):
        print(f"Usage: python3 {sys.argv[0]} <file to ROT> <rotation>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')
