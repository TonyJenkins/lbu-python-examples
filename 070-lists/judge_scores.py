#!/usr/bin/env python3

from statistics import mean


if __name__ == "__main__":
    NUMBER_OF_JUDGES = 6

    marks = []

    while len(marks) < 6:
        try:
            marks.append(int(input(f"Enter Next Judge's Score: ")))
        except ValueError:
            break

    marks.sort()

    print()
    print(f"Average Score: {mean(marks[1:-1]):.2f}")
