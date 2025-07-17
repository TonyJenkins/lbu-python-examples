#!/usr/bin/env python3


import sys


if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as infile:
            file_content = infile.readlines()
    except IndexError:
        print(f'Usage: python3 {sys.argv[0]} <file to uniq>')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}" Sorry about that.')

    else:
        with open(sys.argv[1], 'w') as outfile:
            for line in set(file_content):
                outfile.write(str(line))
        