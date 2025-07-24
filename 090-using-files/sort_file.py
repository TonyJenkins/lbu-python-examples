#!/usr/bin/env python3

import sys


def sort_a_file(filename):
    with open(filename, "r") as infile:
        file_content = infile.readlines()

    with open(filename, "w") as outfile:
        for line in sorted(file_content):
            outfile.write(str(line))


if __name__ == "__main__":
    try:
        sort_a_file(sys.argv[1])
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <file to sort>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')
