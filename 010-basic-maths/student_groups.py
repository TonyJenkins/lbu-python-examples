#!/usr/bin/env python3

if __name__ == "__main__":
    GROUP_SIZE = 24

    number_of_students = 113
    full_groups = number_of_students // GROUP_SIZE
    left_over = number_of_students % GROUP_SIZE

    print(
        f"With {number_of_students} students, and groups of {GROUP_SIZE} students, "
        f"there are {full_groups} full groups, and {left_over} students in a smaller group."
    )
