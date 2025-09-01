#!/usr/bin/env python3

if __name__ == "__main__":
    total_marks = 0
    count_of_marks = 0

    while True:
        try:
            this_mark = int(input(f"Enter Next Grade (Enter to end): "))
            total_marks += this_mark
            count_of_marks += 1
        except ValueError:
            break

    print()
    try:
        print(f"Average Grade: {total_marks / count_of_marks:.2f}")
    except ZeroDivisionError:
        print("No marks entered. No average.")
