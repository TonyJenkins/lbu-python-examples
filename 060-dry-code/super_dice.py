#!/usr/bin/env pytho3

from super_die import super_die


def roll_many_dice(number_to_roll=6, sides=6):
    roll_result = ""
    roll_total = 0

    for _ in range(number_to_roll):
        this_roll = super_die(sides)

        roll_result += str(this_roll) + ", "
        roll_total += this_roll

    return roll_result[:-2], roll_total


if __name__ == "__main__":
    rolls, total = roll_many_dice()
    print(f"{rolls} -> {total}")

    rolls, total = roll_many_dice(12)
    print(f"{rolls} -> {total}")

    rolls, total = roll_many_dice(12, 10)
    print(f"{rolls} -> {total}")
