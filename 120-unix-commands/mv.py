#!/usr/bin/env python3

from os import unlink
import sys


if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as infile, open(sys.argv[2], "w") as outfile:
            outfile.write(infile.read())
            unlink(sys.argv[1])
    except (
        IndexError,
        FileNotFoundError,
    ):
        print(f"Usage: python3 {sys.argv[0]} <original file> <destination file>")
