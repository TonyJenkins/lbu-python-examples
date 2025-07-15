#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    try:
        with open(sys.argv[1], 'r') as first, open(sys.argv[2], 'r') as second:
            if first.read() == second.read():
                print('Files are the same.')
            else:
                print('Files are different')
    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument(s).')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Error opening files to compare.')
