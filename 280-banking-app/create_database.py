#!/usr/bin/env python3

from sqlite3 import OperationalError

from conf import DATABASE_FILE
from db_common import connect, disconnect


def create_user_table(db_file=DATABASE_FILE):
    conn = connect(db_file)

    if conn:
        try:
            conn.execute("""drop table if it exists transactions""")
        except OperationalError:
            pass
        finally:
            conn.execute(
                """create table if not exists transactions(
            id integer primary key autoincrement,
            date_posted datetime not null,
            amount integer not null,
            credit_or_debit text not null)"""
            )

    disconnect(conn)


if __name__ == "__main__":
    create_user_table()
