#!/usr/bin/env python3

from db_common import connect, disconnect
from utils import get_username, get_encrypted_password
from sql_queries import GET_USER_PASSWORD


def do_a_login():
    conn = connect()
    cur = conn.cursor()

    cur.execute(GET_USER_PASSWORD, (get_username(),))
    encrypted_password = cur.fetchone()

    if encrypted_password:
        password = get_encrypted_password()
        if password == encrypted_password[0]:
            print("Access Granted")
        else:
            print("Access Denied")
    else:
        print("Access Denied")

    conn.commit()

    disconnect(conn)


if __name__ == "__main__":
    do_a_login()
