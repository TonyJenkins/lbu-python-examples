#!/usr/bin/env python3

from statistics import mean, StatisticsError


if __name__ == "__main__":
    marks = []

    while True:
        try:
            marks.append(int(input(f"Enter Next Grade (Enter to end): ")))
        except ValueError:
            break

    print()

    try:
        print(f"Average Grade: {mean(marks):.2f}")
    except StatisticsError:
        print("No marks entered. No average.")
