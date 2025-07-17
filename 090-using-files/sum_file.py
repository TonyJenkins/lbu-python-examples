#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    sum = 0

    try:
        with open(sys.argv[1], 'r') as infile:
            for line in infile:
                sum += int(line)
    except IndexError:
        print(f'Usage: python3 {sys.argv[0]} <file to sum>')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')

    else:
        print(f'Sum of "{sys.argv[1]}" is {sum}.')
        