#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    line_no = 1

    try:
        with open(sys.argv[1], 'r') as infile:
            for line in infile:
                print(f'{line_no:5} {line}', end='')
                line_no += 1
    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument.')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')
