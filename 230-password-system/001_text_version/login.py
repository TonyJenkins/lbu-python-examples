#!/usr/bin/env python3


from getpass import getpass

from passwd_utils import check_user


if __name__ == '__main__':

    user = input('User:     ')
    password = getpass('Password: ')

    print(f'Access {"granted" if check_user(user, password) else "denied"}.')
