#!/usr/bin/env python3


def check_file_exists(file_name):
    try:
        f = open(file_name, "r")
        f.close()

        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":

    file_name = input("Enter file to check: ")

    print(
        f'"{file_name}" does {"not " if not check_file_exists(file_name) else ""}exist!'
    )
