#!/usr/bin/env python3


DELETE_USER_TABLE = """
                        DROP TABLE users
                    """

CREATE_USER_TABLE = """
                        CREATE TABLE IF NOT EXISTS users (
                        id integer PRIMARY KEY,
                        username text NOT NULL UNIQUE,
                        name text NOT NULL,
                        password text NOT NULL,
                        admin boolean NOT NULL
                        )
                    """

CREATE_USER = """
                        INSERT INTO users (username, name, password, admin)
                        VALUES (?, ?, ?, ?)
                    """

DELETE_USER = """
                        DELETE FROM users
                        WHERE username = ?
                    """

GET_ALL_USERS = """
                        SELECT * FROM users
                    """

GET_USER_PASSWORD = """
                        SELECT password
                        FROM users
                        WHERE username = ?
                    """

CHANGE_USER_PASSWORD = """
                        UPDATE users
                        SET password = ?
                        WHERE username = ?
                    """

if __name__ == "__main__":
    pass
