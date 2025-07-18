#!/usr/bin/env python3

from tabulate import tabulate

from db_common import connect, disconnect
from sql_queries import GET_ALL_USERS


def print_user_table(user_list):

    clean_list = []
    for user in user_list:
        clean_list.append((user[0], user[1], user[2], '#####', 'Yes' if user[4] else 'No',))

    print(tabulate(clean_list, headers=['uid', 'Username', 'Name', 'Password', 'Admin',], tablefmt='grid'))


if __name__ == '__main__':

    conn = connect()
    cur = conn.cursor()

    cur.execute(GET_ALL_USERS)
    users = cur.fetchall()

    if users:
        print_user_table(users)
    else:
        print('No users in the database!')

    conn.commit()
    disconnect(conn)
