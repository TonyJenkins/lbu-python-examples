#!/usr/bin/env python3

if __name__ == "__main__":
    total_minutes = int(input("Enter the total number of minutes: "))

    hours = total_minutes // 60
    minutes_left = total_minutes % 60

    print(f"{total_minutes} minutes is {hours} hours and {minutes_left} minutes.")
