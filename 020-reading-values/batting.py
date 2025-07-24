#!/usr/bin/env python3

if __name__ == "__main__":
    times_batted = int(input("Enter the number of times batted:  "))
    times_not_out = int(input("Enter the number of times not out: "))
    runs_scored = int(input("Enter the number of runs scored:   "))

    batting_average = runs_scored / (times_batted - times_not_out)

    print(f"That Player's Batting Average is {batting_average:.2f}.")
