#!/usr/bin/env python3

from random import choice as pick
from string import ascii_letters as letters

from conf import SCRABBLE_WORD_LIST


SCRABBLE_SCORES = {
    "a": 1,
    "e": 1,
    "i": 1,
    "l": 1,
    "n": 1,
    "o": 1,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "d": 2,
    "g": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "k": 5,
    "j": 8,
    "x": 8,
    "q": 10,
    "z": 10,
}

SCRABBLE_FREQUENCY = {
    "a": 9,
    "b": 2,
    "c": 2,
    "d": 4,
    "e": 12,
    "f": 2,
    "g": 3,
    "h": 2,
    "i": 9,
    "j": 1,
    "k": 1,
    "l": 4,
    "m": 2,
    "n": 6,
    "o": 8,
    "p": 2,
    "q": 1,
    "r": 6,
    "s": 4,
    "t": 6,
    "u": 4,
    "v": 2,
    "w": 2,
    "x": 1,
    "y": 2,
    "z": 1,
}


def create_pool():
    letters = []
    for letter, count in SCRABBLE_FREQUENCY.items():
        letters.extend([letter] * count)

    return letters


def take_seven_letters(pool):
    rack = []

    while len(rack) < 7:
        letter = pick(pool)
        pool.remove(letter)
        rack.append(letter)

    return rack


def can_make_word_from_rack(rack, word):

    temp_rack = rack[:]

    if len(word) > len(temp_rack):
        return False

    for letter in word:
        if letter not in temp_rack:
            return False
        else:
            temp_rack.remove(letter)

    return True


def possible_words_from_rack(rack):
    possible_words = []

    for word in open(SCRABBLE_WORD_LIST, "r").readlines():
        if can_make_word_from_rack(rack, word.strip()):
            possible_words.append(word.strip())

    return possible_words


def letter_score(letter):
    if letter in letters:
        return SCRABBLE_SCORES.get(letter.lower())
    else:
        return 0


def word_score(word):

    score = 0

    for letter in word:
        score += letter_score(letter)

    if len(word) == 7:
        score += 50

    return score


if __name__ == "__main__":

    rack = take_seven_letters(create_pool())
    print(f"Rack: {rack}")

    for word in possible_words_from_rack(rack):
        print(f"{word:10} {word_score(word)}")
