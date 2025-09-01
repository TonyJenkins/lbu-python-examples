#!/usr/bin/env python3

if __name__ == "__main__":
    FAILS_ALLOWED = 3

    fails = 0

    while True:
        password = input("Enter password: ")
        confirm = input("Confirm:        ")

        if password == confirm:
            print("Passwords match!")
            break
        else:
            fails += 1
            if fails < FAILS_ALLOWED:
                print(f"Try again. {FAILS_ALLOWED - fails} attempt(s) left.")
            else:
                print("Error. No match and no more attempts.")
                break
