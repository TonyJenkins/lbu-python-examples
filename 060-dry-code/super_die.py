#!/usr/bin/env python3


def super_die(sides=6):
    from random import randint

    if sides < 2:
        raise ValueError("Invalid number of sides")

    return randint(1, sides)


if __name__ == "__main__":
    for test_sides in [2, 8, 24]:
        for _ in range(4):
            print(f"Sides: {test_sides}, Roll: {super_die(test_sides)}")
            print()
