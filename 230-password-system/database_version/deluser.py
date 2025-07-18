#!/usr/bin/env python3

from db_common import connect, disconnect
from sql_queries import DELETE_USER
from utils import get_username


if __name__ == '__main__':

    conn = connect()
    cur = conn.cursor()

    cur.execute(DELETE_USER, (get_username(),))

    conn.commit()

    print(f'User {"deleted" if cur.rowcount else "not found"}.')

    disconnect(conn)
