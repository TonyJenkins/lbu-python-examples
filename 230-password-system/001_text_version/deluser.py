#!/usr/bin/env python3


from passwd_utils import delete_user
from passwd_utils import UserDeleteError


if __name__ == '__main__':

    user = input('Enter username: ')

    try:
        delete_user(user)
        print('User Deleted.')
    except UserDeleteError:
        print('Cannot delete. Most likely username does not exist.')
