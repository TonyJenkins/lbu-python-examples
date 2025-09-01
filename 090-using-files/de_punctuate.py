#!/usr/bin/env python3

import sys


def remove_non_letters(s):
    from string import punctuation

    return "".join([c for c in s if c not in punctuation])


def depunctuate_a_file(filename):
    with open(filename, "r") as infile:
        file_content = infile.read()

        with open(filename, "w") as outfile:
            outfile.write(remove_non_letters(file_content))


if __name__ == "__main__":
    try:
        depunctuate_a_file(sys.argv[1])
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <file to clean>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')
