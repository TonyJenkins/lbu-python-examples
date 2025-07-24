#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    try:
        with open(sys.argv[1]) as infile:
            for line in infile:
                print(line[:-1])
    except (
        IndexError,
        FileNotFoundError,
    ):
        print(f"Usage: python3 {sys.argv[0]} <file to display>")
