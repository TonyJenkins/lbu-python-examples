#!/usr/bin/env python3

if __name__ == "__main__":
    COUNTDOWN_START = 10

    for second in range(COUNTDOWN_START, 0, -1):
        print(f"{second:2} ...")

    print("Lift Off!")
