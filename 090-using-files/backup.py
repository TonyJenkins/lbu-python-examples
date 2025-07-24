#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as infile, open(
            sys.argv[1] + ".bak", "w"
        ) as outfile:
            outfile.write(infile.read())
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <file to backup>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')
