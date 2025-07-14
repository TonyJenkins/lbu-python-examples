#!/usr/bin/env python3

from random import randint


def choose_secret_number():
    while True:
        secret = randint(0, 100)
        if secret not in [25, 50, 75]:
            return secret
        

def get_guess(number_of_guesses):
    while True:
        try:
            next_guess = int(input(f'Enter guess #{number_of_guesses + 1}: '))
            if next_guess < 0 or next_guess > 100:
                print('Please guess numbers between 0 and 100!')
            else:
                return next_guess
        except ValueError:
            print('Please enter an integer!')


def print_game_status(secret, guess):
    if secret > guess:
        print('My number is higher than your guess.')
    elif secret < guess:
        print('My number is lower than your guess.')
    else:
        print('You guessed the number!')


def game_over(secret, guess):
    return secret == guess


def play_game():
    print('Amazing Hi-Lo Game')
    print('==================')
    print()

    secret_number = choose_secret_number()
    guesses_so_far = 0

    while True:
        new_guess = get_guess(guesses_so_far)

        print_game_status(secret_number, new_guess)
        if game_over(secret_number, new_guess):
            break
        else:
            guesses_so_far += 1


if __name__ == '__main__':
    play_game()
    