#!/usr/bin/env python3

from sqlite3 import OperationalError

from banking_exception import BankingError
from conf import DATABASE_FILE
from db_common import connect, disconnect


def get_current_balance(db_file=DATABASE_FILE):
    conn = connect(db_file)

    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                """select date_posted, amount, credit_or_debit from transactions order by date_posted asc"""
            )
            conn.commit()

            balance = 0
            for transaction in cur:
                date, amount, credit_or_debit = transaction
                if credit_or_debit == "CR":
                    balance += amount
                elif credit_or_debit == "DB":
                    balance -= amount

            return balance

        except OperationalError as e:
            print(f"An error occurred: {e}")
        finally:
            disconnect(conn)

        return None


if __name__ == "__main__":
    try:
        current_balance = get_current_balance()
        print(
            f'Balance: {abs(current_balance)} {"CR" if current_balance >= 0 else "DB"}'
        )
    except BankingError as be:
        print(be.message())
