#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        total_minutes = int(input("Enter the total number of minutes: "))
    except ValueError:
        print("Error! Numeric value needed.")
    else:
        if total_minutes >= 0:
            hours = total_minutes // 60
            minutes_left = total_minutes % 60

            print(
                f"{total_minutes} minutes is {hours} hours and {minutes_left} minutes."
            )
        else:
            print("Please enter a non-negative number of minutes.")
