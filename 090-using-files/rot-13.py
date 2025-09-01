#!/usr/bin/env python3

import sys


def rot_13_character(c):
    from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase

    if not c.isalpha():
        return c

    letters = lowercase if c.islower() else uppercase

    rot13_alphabet = letters[13:] + letters[:13]

    return rot13_alphabet[letters.find(c)]


def rot_13_string(s):
    return "".join([rot_13_character(c) for c in s])


def rot_13_file(filename):
    with open(filename, "r") as infile:
        file_content = infile.read()

    with open(filename, "w") as outfile:
        outfile.write(rot_13_string(file_content))


if __name__ == "__main__":
    try:
        rot_13_file(sys.argv[1])
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <file to ROT>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')
