#!/usr/bin/env python3

if __name__ == "__main__":
    NUMBERS_PER_LINE = 5

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{'FizzBuzz'}", end="")
        elif number % 3 == 0:
            print(f"{'Fizz':<8}", end="")
        elif number % 5 == 0:
            print(f"{'Buzz':<8}", end="")
        else:
            print(f"{number:<8}", end="")

        if number % NUMBERS_PER_LINE == 0:
            print()
