#!/usr/bin/env python3

import sys


def sum_a_file_of_numbers(filename):
    total = 0

    with open(filename, "r") as infile:
        for line in infile:
            total += int(line.strip())

    return total


if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as infile:
            print(f'Sum of "{sys.argv[1]}" is {sum_a_file_of_numbers(sys.argv[1])}')
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <file to sum>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')
