#!/usr/bin/env python3

from os import unlink
import sys


if __name__ == "__main__":
    try:
        unlink(sys.argv[1])
    except (
        IndexError,
        FileNotFoundError,
    ):
        print(f"Usage: python3 {sys.argv[0]} <file to remove>")
