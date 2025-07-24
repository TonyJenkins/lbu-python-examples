#!/usr/bin/env python3

import sys


def check_file(file_to_check):
    from os import listdir
    from os.path import isfile

    files_that_exist = [f for f in listdir(".") if isfile(f)]
    return file_to_check in files_that_exist


if __name__ == "__main__":
    try:
        if check_file(sys.argv[1]):
            print(f'"{sys.argv[1]}" found!')
        else:
            print(f'"{sys.argv[1]}" not found!')
    except IndexError:
        print(f"Usage: python3 {sys.aegv[0]} <file to check>")
