#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    lines = words = characters = 0

    try:
        with open(sys.argv[1], 'r') as infile:
            for line in infile.readlines():
                lines += 1
                words += len(line.split())
                characters += len(line)

        print(f'Lines:      {lines:6}')
        print(f'Words:      {words:6}')
        print(f'Characters: {characters:6}')

    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument.')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')
