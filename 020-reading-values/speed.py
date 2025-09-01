#!/usr/bin/env python3

if __name__ == "__main__":
    distance = int(input("Enter the distance in miles: "))
    time = int(input("Enter the time in minutes:   "))

    mph = distance / (time / 60)

    print(
        f"Travelling {distance} miles in {time} minutes is equivalent to {mph:.2f} mph."
    )
