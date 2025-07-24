#!/usr/bin/env python3

if __name__ == "__main__":
    distance = 100
    time = 140

    mph = distance / (time / 60)

    print(
        f"Travelling {distance} miles in {time} minutes is equivalent to {mph:.2f} mph."
    )
