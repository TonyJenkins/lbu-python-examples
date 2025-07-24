#!/usr/bin/env python3


from random import choice


def play_the_quiz_game(capitals=None):
    if capitals is None:
        capitals = {}

    while True:
        country = choice(list(capitals))

        answer = input(f"Enter the capital of {country.title()}: ")
        if answer.lower() == capitals[country]:
            print("Correct!")
            print("You get to enter another!")
            new_country = input("Enter a country: ").lower()
            new_capital = input("Enter the capital: ").lower()

            capitals[new_country] = new_capital

        else:
            print(
                f"Incorrect. The capital of {country.title()} is {capitals[country].title()}"
            )

        print()

        again = input("Try Again? (y/n) ")
        if again == "n":
            break


if __name__ == "__main__":
    CAPITALS = {
        "england": "london",
        "scotland": "edinburgh",
        "ireland": "dublin",
    }

    play_the_quiz_game(CAPITALS)
