#!/usr/bin/env python3

from passwd_utils import add_user_to_file
from passwd_utils import UserExistsError


def add_a_user():
    user = input("Enter new username: ")
    name = input("Enter real name:    ")
    password = input("Enter password:     ")

    if not user or not name or not password:
        print("Cannot add. Missing data.")
    else:
        try:
            add_user_to_file(
                (
                    user,
                    name,
                    password,
                )
            )
            print("User Created.")
        except UserExistsError:
            print("Cannot add. Most likely username already exists.")


if __name__ == "__main__":
    add_a_user()
