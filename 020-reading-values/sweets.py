#!/usr/bin/env python3

if __name__ == "__main__":
    number_of_friends = int(input("How many friends do you have? "))
    number_of_sweets = int(input("How many sweets do you have?  "))

    sweets_each = number_of_sweets // number_of_friends
    left_over = number_of_sweets % number_of_friends

    print(
        f"With {number_of_friends} friends, and {number_of_sweets} sweets, "
        f"everyone gets {sweets_each} sweets, and there will be {left_over} left over."
    )
