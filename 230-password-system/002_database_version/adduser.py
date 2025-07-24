#!/usr/bin/env python3

from sqlite3 import IntegrityError

from db_common import connect, disconnect
from sql_queries import CREATE_USER
from utils import get_y_or_n, get_username, get_encrypted_password


def get_user_details():
    username = get_username(2, 8)
    name = input("Real Name: ")
    password = get_encrypted_password()
    admin = get_y_or_n("Admin? (y/n): ")

    return username, name, password, True if admin == "y" else False


def add_a_user():
    conn = connect()

    try:
        conn.execute(CREATE_USER, get_user_details())
    except IntegrityError:
        print("Failed to add user. Most likely the user already exists.")
    finally:
        conn.commit()

    disconnect(conn)


if __name__ == "__main__":
    add_a_user()
