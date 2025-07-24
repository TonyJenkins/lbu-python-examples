#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as infile:
            line_no = 1
            for line in infile:
                print(f"{line_no:5} {line}", end="")
                line_no += 1
    except (
        IndexError,
        FileNotFoundError,
    ):
        print(f"Usage: python3 {sys.argv[0]} <file to display>")
