#!/usr/bin/env python3

from sqlite3 import OperationalError

from conf import DATABASE_FILE
from db_common import connect, disconnect

from sql_queries import CREATE_USER_TABLE, DELETE_USER_TABLE


def create_user_table(db_file=DATABASE_FILE):
    conn = connect(db_file)

    if conn:
        try:
            conn.execute(DELETE_USER_TABLE)
        except OperationalError:
            pass
        finally:
            conn.execute(CREATE_USER_TABLE)

    disconnect(conn)


if __name__ == "__main__":
    create_user_table()
