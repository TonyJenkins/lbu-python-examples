#!/usr/bin/env python3

from random import choice


if __name__ == "__main__":
    try:
        tosses = int(input("How many coin tosses would you like to simulate? "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if tosses < 1:
            print("Please enter a positive integer.")
        else:
            print(f"Simulating {tosses} coin tosses...")

            heads_count = tails_count = 0

            for _ in range(tosses):
                result = choice(["Heads", "Tails"])
                if result == "Heads":
                    heads_count += 1
                else:
                    tails_count += 1

            print(
                f"Heads: {heads_count} ({heads_count / tosses * 100:.2f}%), "
                f"Tails: {tails_count} ({tails_count / tosses * 100:.2f}%)"
            )
