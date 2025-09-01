#!/usr/bin/env python3

from random import choice


if __name__ == "__main__":
    result = choice(["Heads", "Tails"])

    print(f"The coin landed on: {result}")
