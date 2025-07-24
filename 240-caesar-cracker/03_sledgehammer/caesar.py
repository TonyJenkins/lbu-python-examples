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


if __name__ == "__main__":

    try:
        with open(sys.argv[1], "r") as infile:
            file_content = infile.read()
            rotation = int(sys.argv[2])
    except (
        IndexError,
        ValueError,
    ):
        print(f"Usage: python3 {sys.argv[0]} <file to ROT> <rotation>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')

    else:
        with open(sys.argv[1], "w") as rotfile:
            rotfile.write(rot_string(file_content, rotation))
