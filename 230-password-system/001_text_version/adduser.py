#!/usr/bin/env python3


from passwd_utils import add_user_to_file
from passwd_utils import UserExistsError


if __name__ == '__main__':

    user = input('Enter new username: ')
    name = input('Enter real name:    ')
    password = input('Enter password:     ')

    try:
        add_user_to_file((user, name, password))
        print('User Created.')
    except UserExistsError:
        print('Cannot add. Most likely username already exists.')
