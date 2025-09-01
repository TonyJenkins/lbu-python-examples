#!/usr/bin/env python3

from sqlite3 import OperationalError
import sys

from banking_exception import BankingError
from conf import DATABASE_FILE
from db_common import connect, disconnect


def make_a_deposit(amount, db_file=DATABASE_FILE):
    conn = connect(db_file)

    if conn:
        try:
            conn.execute(
                """insert into transactions (date_posted, amount, credit_or_debit)
                values (datetime('now'), ?, ?)""",
                (amount, "CR"),
            )
            conn.commit()
        except OperationalError as e:
            raise BankingError("Cannot make a deposit")
        finally:
            disconnect(conn)


if __name__ == "__main__":
    try:
        make_a_deposit(int(sys.argv[1]))
    except BankingError as be:
        print(be.message)
