#!/usr/bin/env python3

from codecs import encode
from getpass import getpass


def get_y_or_n(prompt="Enter 'y' or 'n'"):
    while True:
        entry = input(prompt)
        if entry in "yn":
            return entry
        else:
            print("Please enter 'y' or 'n'")


def get_username(min_length=2, max_length=8):
    while True:
        username = input("Enter username: ")
        if username.islower():
            if min_length <= len(username) <= max_length:
                return username
            else:
                print(
                    f"Error: username must be between "
                    f"{min_length} and {max_length} characters"
                )
        else:
            print("Error: username must be lower case")


def encrypt(password):
    return encode(password, "rot13")


def get_encrypted_password(prompt="Password: "):
    return encrypt(getpass(prompt))


def check_password(encrypted_password, plain_password):
    return encrypt(plain_password) == encrypted_password
