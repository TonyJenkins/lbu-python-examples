#!/usr/bin/env python3

from codecs import encode


class UserExistsError(Exception):
    pass


class UserDeleteError(Exception):
    pass


class PasswordUpdateError(Exception):
    pass


PASSWORD_FILE = 'passwd.txt'


def encrypt(password):
    return encode(password, 'rot13')


def check_password(encrypted_password, password):
    return encrypt(password) == encrypted_password


def read_password_file():

    users = []

    with open(PASSWORD_FILE, 'r') as p:
        for line in p:
            username, real_name, password = line.strip().split(':')
            users.append((username, real_name, password,))

    return users


def write_password_file(user_list):

    with open(PASSWORD_FILE, 'w') as p:
        for user in user_list:
            p.write(f'{user[0]}:{user[1]}:{user[2]}\n')


def user_exists(username):
    current_users = read_password_file()

    for line in current_users:
        name, real_name, password = line
        if name == username:
            return True

    return False


def add_user_to_file(user_info):

    name, real_name, raw_password = user_info

    if user_exists(name):
        raise UserExistsError('User to add already exists')

    password = encrypt(raw_password)

    current_users = read_password_file()
    current_users.append((name, real_name, password))

    write_password_file(current_users)


def delete_user(username):

    if not user_exists(username):
        raise UserDeleteError('Delete target user does not exist')

    current_users = read_password_file()

    new_users = [
        user
        for user in current_users
        if user[0] != username
    ]

    write_password_file(new_users)


def check_user(username, password):
    current_users = read_password_file()

    for user in current_users:
        if user[0] == username and check_password(user[2], password):
            return True

    return False


def change_password(username, password):

    if not user_exists(username):
        raise PasswordUpdateError('Attempt to change password for invalid user')

    current_users = read_password_file()

    new_users = []

    for user in current_users:
        if user[0] == username:
            new_users.append((username, user[1], encrypt(password),))
        else:
            new_users.append(user)

    write_password_file(new_users)


if __name__ == '__main__':
    print(read_password_file())

    users = read_password_file()
    write_password_file(users)
