#!/usr/bin/env python3

from random import randint

NUMBER_OF_NUMBERS = 1000

MAX_NUMBER = 100
MIN_NUMBER = 0

FILE_NAME = "numbers.txt"

if __name__ == "__main__":
    with open(FILE_NAME, "w") as of:
        for _ in range(NUMBER_OF_NUMBERS):
            of.write(str(randint(MIN_NUMBER, MAX_NUMBER)))
            of.write("\n")
