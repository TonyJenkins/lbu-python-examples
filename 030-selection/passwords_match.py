#!/usr/bin/env python3

if __name__ == "__main__":
    password = input("Enter the new password:   ")
    confirm = input("Confirm the new password: ")

    if password == confirm:
        print(f"Passwords match!")
    else:
        print(f"Passwords do not match! Please try again.")
