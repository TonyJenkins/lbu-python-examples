#!/usr/bin/env python3

if __name__ == "__main__":
    NUMBER_OF_GRADES = 5

    total_grades = 0

    for count in range(NUMBER_OF_GRADES):
        this_grade = int(input(f"Enter Grade #{count + 1}: "))
        total_grades += this_grade

    print()
    print(f"Average Grade: {total_grades / 5:.2f}")
