#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    try:
        file_name = sys.argv[2]
        pattern = sys.argv[1]

        with open(file_name, 'r') as infile:
            for line in infile:
                if pattern in line:
                    print(line, end='')
    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument.')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[2]}"')
