#!/usr/bin/env python3

from tabulate import tabulate

from db_common import connect, disconnect
from sql_queries import GET_ALL_USERS


def print_user_table(user_list):
    clean_list = [
        [
            "uid",
            "Username",
            "Name",
            "Password",
            "Admin",
        ],
    ]

    for user in user_list:
        uid, username, name, _, admin = user
        clean_list.append(
            ([
                uid,
                username,
                name,
                "#####",
                "Yes" if admin else "No",
            ])
        )

    print(tabulate(clean_list, headers="firstrow", tablefmt="grid"))


def list_all_the_users():
    conn = connect()
    cur = conn.cursor()

    cur.execute(GET_ALL_USERS)
    users = cur.fetchall()

    if users:
        print_user_table(users)
    else:
        print("No users in the database!")

    conn.commit()
    disconnect(conn)


if __name__ == "__main__":
    list_all_the_users()
