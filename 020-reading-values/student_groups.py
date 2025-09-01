#!/usr/bin/env python3

if __name__ == "__main__":
    group_size = int(input("Enter the number of students in each group: "))
    number_of_students = int(input("Enter the number of students in the class:  "))

    full_groups = number_of_students // group_size
    left_over = number_of_students % group_size

    print(
        f"With {number_of_students} students, and groups of {group_size} students, "
        f"there are {full_groups} full groups, and {left_over} students in a smaller group."
    )
