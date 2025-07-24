#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        mark = int(input("Enter a mark (0-100): "))

        if 0 < mark < 101:
            print("Mark out of range (0-100)")
        elif mark >= 70:
            print("Grade is Distinction")
        elif mark >= 60:
            print("Grade is Merit")
        elif mark >= 50:
            print("Grade is Pass")
        else:
            print("Grade is Fail")
    except ValueError:
        print("Invalid input, please enter a numeric value.")
