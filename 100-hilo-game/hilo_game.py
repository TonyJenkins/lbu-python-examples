#!/usr/bin/env python3

from random import randint


CHEATING = False

MAX_GUESSES = 10


def choose_secret_number():
    while True:
        secret = randint(0, 100)
        if secret not in [25, 50, 75]:
            if CHEATING:
                print(f"DEBUG: Secret number is {secret} DEBUG")
            return secret


def get_guess(number_of_guesses, already_guessed):
    while True:
        try:
            next_guess = int(input(f"Enter guess #{number_of_guesses + 1}: "))
            if next_guess < 0 or next_guess > 100:
                print("Please guess numbers between 0 and 100!")
            elif next_guess in already_guessed:
                print("You already guessed that number!")
            else:
                return next_guess
        except ValueError:
            print("Please enter an integer!")


def print_game_status(secret, guess):
    if secret > guess:
        print("My number is higher than your guess.")
    elif secret < guess:
        print("My number is lower than your guess.")


def game_over(secret, guess, guesses_taken, max_guesses=10):
    return (secret == guess) or guesses_taken == max_guesses


def print_banner():
    print("Amazing Hi-Lo Game")
    print("==================")
    print()


def print_endgame(secret, last_guess, guesses_taken):
    print()
    print("Game Over!")

    if secret != last_guess:
        print(f"You lose! The secret number was {secret}!")
    elif secret == last_guess:
        print("You win! Well done!")
        print(f"You took {guesses_taken} guess{'es' if guesses_taken != 1 else ''}.")

    print()


def play_game():
    print_banner()

    secret_number = choose_secret_number()
    guesses_so_far = 0
    numbers_guessed = []

    while True:
        new_guess = get_guess(guesses_so_far, numbers_guessed)
        guesses_so_far += 1
        numbers_guessed.append(new_guess)

        print_game_status(secret_number, new_guess)

        if game_over(secret_number, new_guess, guesses_so_far, MAX_GUESSES):
            print_endgame(secret_number, new_guess, guesses_so_far)
            break


if __name__ == "__main__":
    play_game()
