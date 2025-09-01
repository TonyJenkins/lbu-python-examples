#!/usr/bin/env python3

if __name__ == "__main__":
    NUMBER_OF_GRADES = 6
    PASSES_FOR_OVERALL_PASS = 5

    PASS_GRADE = 40

    passed_modules = 0

    for count in range(NUMBER_OF_GRADES):
        this_grade = int(input(f"Enter Grade #{count + 1}: "))
        if this_grade >= PASS_GRADE:
            passed_modules += 1

    print()
    if passed_modules >= PASSES_FOR_OVERALL_PASS:
        print("Student has passed overall!")
    else:
        print("Student has failed overall. How sad.")
