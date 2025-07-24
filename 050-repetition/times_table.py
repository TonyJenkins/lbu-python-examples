#!/usr/bin/env python3

if __name__ == "__main__":
    table_wanted = int(input("Which table would you like to see? "))

    print()
    print(f"The {table_wanted} Times Table")
    print()

    for term in range(13):
        print(f"{term:>2} x {table_wanted} = {term * table_wanted:>3}")
