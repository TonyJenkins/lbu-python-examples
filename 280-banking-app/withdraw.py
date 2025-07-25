#!/usr/bin/env python3

from sqlite3 import OperationalError
import sys

from banking_exception import BankingError
from conf import DATABASE_FILE
from db_common import connect, disconnect


def make_a_withdrawal(amount, db_file=DATABASE_FILE):
    conn = connect(db_file)

    if conn:
        try:
            conn.execute(
                """insert into transactions (date_posted, amount, credit_or_debit)
                values (datetime('now'), ?, ?)""",
                (amount, "DB"),
            )
            conn.commit()
        except OperationalError as e:
            raise BankingError("Cannot make do that withdrawal")
        finally:
            disconnect(conn)


if __name__ == "__main__":
    try:
        make_a_withdrawal(int(sys.argv[1]))
    except BankingError as be:
        print(be.message)
