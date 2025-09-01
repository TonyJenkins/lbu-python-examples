#!/usr/bin/env python3

if __name__ == "__main__":
    password = input("Enter the new password:   ")
    confirm = input("Confirm the new password: ")

    if password == confirm and 8 <= len(password) <= 12:
        print(f"Password Changed!")
    elif password == confirm and (len(password) < 8 or len(password) > 12):
        print(f"Password is invalid length! Please try again.")
    else:
        print(f"Passwords do not match! Please try again.")
