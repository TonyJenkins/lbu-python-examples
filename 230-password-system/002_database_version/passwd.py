#!/usr/bin/env python3

from db_common import connect, disconnect
from utils import get_username, get_encrypted_password
from sql_queries import GET_USER_PASSWORD, CHANGE_USER_PASSWORD


def change_a_password():
    conn = connect()
    cur = conn.cursor()

    user = get_username()

    cur.execute(GET_USER_PASSWORD, (user,))
    encrypted_password = cur.fetchone()

    if encrypted_password:
        old_password = get_encrypted_password("Current Password: ")
        if old_password == encrypted_password[0]:
            new_password = get_encrypted_password("New Password: ")
            new_password_reentry = get_encrypted_password("Re-enter: ")
            if new_password == new_password_reentry:
                cur.execute(
                    CHANGE_USER_PASSWORD,
                    (
                        new_password,
                        user,
                    ),
                )
                print("Password Updated")
            else:
                print("Password mismatch. Password unchanged.")
        else:
            print("Current Password Incorrect")
    else:
        print("Unknown User")

    conn.commit()

    disconnect(conn)


if __name__ == "__main__":
    change_a_password()
