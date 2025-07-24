#!/usr/bin/env python3

from codecs import encode


class UserExistsError(Exception):
    pass


class UserDeleteError(Exception):
    pass


class PasswordUpdateError(Exception):
    pass


PASSWORD_FILE = "passwd.txt"


def encrypt(password):
    return encode(password, "rot13")


def validate_password(encrypted_password, password):
    return encrypt(password) == encrypted_password


def read_password_file():
    users = []

    with open(PASSWORD_FILE, "r") as pf:
        for line in pf:
            username, real_name, password = line.strip().split(":")
            users.append(
                (
                    username,
                    real_name,
                    password,
                )
            )

    return users


def write_password_file(user_list):

    with open(PASSWORD_FILE, "w") as pf:
        for user in user_list:
            pf.write(f"{':'.join(user)}" + "\n")


def user_exists(username):
    current_users = read_password_file()

    for user in current_users:
        user_id, _, __ = user
        if user_id == username:
            return True

    return False


def add_user_to_file(user_info):
    user_id, real_name, raw_password = user_info

    if user_exists(id):
        raise UserExistsError("User to add already exists")

    encrypted_password = encrypt(raw_password)

    current_users = read_password_file()
    current_users.append((user_id, real_name, encrypted_password))

    write_password_file(current_users)


def delete_user(username):
    if not user_exists(username):
        raise UserDeleteError("Delete target user does not exist")

    current_users = read_password_file()

    new_users = [user for user in current_users if user[0] != username]

    write_password_file(new_users)


def check_user(username, password):
    current_users = read_password_file()

    for user in current_users:
        check_username, _, check_password = user
        if check_username == username and validate_password(check_password, password):
            return True

    return False


def change_password(username, password):
    if not user_exists(username):
        raise PasswordUpdateError("Attempt to change password for invalid user")

    current_users = read_password_file()

    new_users = []

    for user in current_users:
        id, real_name, _ = user
        if id == username:
            new_users.append(
                (
                    username,
                    real_name,
                    encrypt(password),
                )
            )
        else:
            new_users.append(user)

    write_password_file(new_users)


if __name__ == "__main__":
    print(read_password_file())

    users_temp = read_password_file()
    write_password_file(users_temp)
