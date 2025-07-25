#!/usr/bin/env python3

from conf import DATABASE_FILE
import sqlite3


def connect(db_file=DATABASE_FILE):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)


def disconnect(connection):
    connection.close()
