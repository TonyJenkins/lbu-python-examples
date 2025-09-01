#!/usr/bin/env python3

from sqlite3 import OperationalError

import tabulate

from banking_exception import BankingError
from conf import DATABASE_FILE
from db_common import connect, disconnect


def print_statement(db_file=DATABASE_FILE):
    conn = connect(db_file)

    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                """select id, date_posted, amount, credit_or_debit from transactions order by date_posted asc"""
            )
            conn.commit()

            transactions = cur.fetchall()
            transactions.insert(0, ("Ref", "Date", "Amount", "Type"))

            print(tabulate.tabulate(transactions, headers="firstrow", tablefmt="grid"))
        except OperationalError as e:
            print(f"An error occurred: {e}")
        finally:
            disconnect(conn)


if __name__ == "__main__":
    try:
        print_statement()
    except BankingError as be:
        print(be.message())
