#!/usr/bin/env python3


class CaesarException(Exception):
    pass


from caesar import rot_string

import sys


FILE_OF_ALL_WORDS = "words_alpha.txt"


def clean_text(text):
    from string import punctuation

    for c in punctuation + "\n" + "\t":
        text = text.replace(c, " ")

    return " ".join(text.split())


def extract_words(text):
    return clean_text(text.lower()).split()


def load_dictionary_of_words(word_file=FILE_OF_ALL_WORDS):
    with open(word_file, "r") as w:
        words = [word.strip() for word in w.readlines()]

    return words


def check_shifted_words(words, word_file=FILE_OF_ALL_WORDS):
    valid_words = load_dictionary_of_words(word_file)

    percent_real_words = {}

    for shift in range(1, 26):

        valid_count = 0

        for word in words:
            if rot_string(word, -shift) in valid_words:
                valid_count += 1

        percent_real_words[shift] = valid_count / len(words)

        if valid_count / len(words) > 0.95:  # Cruft!
            break

    return percent_real_words


def find_correct_shift(shifts_and_percents):
    best_shift = max(shifts_and_percents, key=shifts_and_percents.get)

    if shifts_and_percents[best_shift] > 0.95:
        return best_shift

    raise CaesarException()


def display_original(message_text, established_shift):
    print(rot_string(message_text, -established_shift))


def crack_the_code(rotted_file):
    try:
        with open(rotted_file, "r") as shifted_file:

            shifted_text = shifted_file.read()
            shifted_words = extract_words(shifted_text)

            shift_used = find_correct_shift(
                check_shifted_words(shifted_words, FILE_OF_ALL_WORDS)
            )

            display_original(shifted_text, shift_used)

    except CaesarException:
        print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")


if __name__ == "__main__":
    try:
        crack_the_code(sys.argv[1])
    except (
        IndexError,
        FileNotFoundError,
    ):
        print(f"Usage: {sys.argv[0]} <file to crack>")
