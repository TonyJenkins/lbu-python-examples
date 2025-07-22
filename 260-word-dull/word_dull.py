#!/usr/bin/env python3


from conf import NUMBER_OF_GUESSES, WORD_FILE


def choose_secret_word(word_list=WORD_FILE):
    from random import choice

    with open(word_list, 'r') as words:
        all_words = words.readlines()

        return choice(all_words).strip().lower()


def word_is_in_list(word_to_check, word_list=WORD_FILE):
    with open(word_list, 'r') as words:
        for every_word in words:
            if word_to_check.lower().strip() == every_word.lower().strip():
                return True

    return False


def mark_guess(guess, secret):

    marks = ['-'] * len(guess)

    guess_list = list(guess.lower())
    secret_list = list(secret.lower())

    for position in range(len(guess)):
        if guess_list[position] == secret_list[position]:
            marks[position] = 'G'
            guess_list[position] = '-'
            secret_list[position] = '-'

    for position in range(len(guess)):
        if guess_list[position] != '-':
            if guess_list[position] in secret_list:
                marks[position] = 'Y'
                secret_list.remove(guess_list[position])

    return ''.join(marks)


def colour_marks(mark_string, guess):
    from colorama import init, Fore, Back

    init()

    output_marks = ''
    for position in range(len(mark_string)):
        mark = mark_string[position]
        if mark == 'G':
            output_marks += Back.GREEN + Fore.BLACK + guess[position].upper() + Fore.RESET + Back.RESET
        elif mark == 'Y':
            output_marks += Back.YELLOW + Fore.BLACK + guess[position].upper() + Fore.RESET + Back.RESET
        else:
            output_marks += Back.WHITE + Fore.BLACK + guess[position].upper() + Fore.RESET + Back.RESET

    return output_marks


def show_banner():
    print()
    print('Welcome to Word Dull!')
    print('=====================')
    print()
    print('Can you guess the secret word?')
    print()


def show_endgame(guesses):
    print()

    match guesses:
        case 1:
            print('Fluke!')
        case 2:
            print('Amazing!')
        case 3 | 4:
            print('Well done!')
        case 5:
            print('Solid work!')
        case 6:
            print('Phew!')

    print()


def play_word_dull():

    show_banner()

    secret = choose_secret_word()
    guesses = 0
    victory = False

    while guesses < NUMBER_OF_GUESSES:
        guess = input(f'({guesses + 1}). Guess a word: > ')

        if word_is_in_list(guess, WORD_FILE):
            guesses += 1

            marking = mark_guess(guess, secret)
            print(colour_marks(marking, guess))

            if guess == secret:
                show_endgame(guesses)
                victory = True
                break

        else:
            print('No such word!')

    if not victory:
        print('Bad luck. Try again tomorrow.')


if __name__ == '__main__':
   play_word_dull()
