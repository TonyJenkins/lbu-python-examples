#!/usr/bin/env python3

from getpass import getpass

from passwd_utils import change_password, check_user


def change_a_password():
    user = input("User:             ")
    password = getpass("Current Password: ")

    if check_user(user, password):
        new_password = getpass("New Password: ")
        confirm_password = getpass("Confirm:      ")

        if new_password == confirm_password:
            change_password(user, new_password)
            print("Password changed.")
        else:
            print("New passwords do not match.")
    else:
        print("User details incorrect. Try again.")


if __name__ == "__main__":
    change_a_password()
