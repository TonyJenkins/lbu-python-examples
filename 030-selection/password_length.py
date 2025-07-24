#!/usr/bin/env python3

if __name__ == "__main__":
    password = input("Enter the new password: ")

    if 8 <= len(password) <= 12:
        print(f"Password length is acceptable: {len(password)} characters.")
    else:
        print(f"Password length is not acceptable: {len(password)} characters.")
