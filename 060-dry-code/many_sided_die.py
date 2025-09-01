#!/usr/bin/env python3

from random import randint


if __name__ == "__main__":
    try:
        sides = int(input("How many sides does the die have? "))
        if sides < 2:
            raise ValueError("Number of sides must be at least 2.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
    else:
        result = randint(1, sides)
        print(f"The die landed on: {result}")
