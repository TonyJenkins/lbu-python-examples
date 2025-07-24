#!/usr/bin/env python3

from passwd_utils import delete_user
from passwd_utils import UserDeleteError


def delete_a_user():
    user = input("Enter username: ")

    if not user:
        print("Cannot delete a user with no name.")
    else:
        try:
            delete_user(user)
            print("User Deleted.")
        except UserDeleteError:
            print("Cannot delete. Most likely username does not exist.")


if __name__ == "__main__":
    delete_a_user()
