#!/usr/bin/env python3

import sys


LINUX_WORD_LIST = "/usr/share/dict/words"
MY_WORD_LIST = "./words_alpha.txt"


def load_dictionary(word_file=MY_WORD_LIST):

    word_list = []

    with open(word_file, "r") as words:
        for word in words.readlines():
            word_list.append(word[:-1])

    return word_list


def clean_word(dirty_word):
    from string import ascii_lowercase as letters

    return "".join([c.lower() if c.lower() in letters else "" for c in dirty_word])


def is_word(possible_word):
    return possible_word.isalpha()


if __name__ == "__main__":
    try:
        real_words = load_dictionary()
    except FileNotFoundError:
        print(f"{sys.argv[0]}: Cannot open the dictionary file.")
    else:
        try:
            with open(sys.argv[1]) as file_to_check:
                for line in file_to_check:
                    for word in line.split():
                        if is_word(word) and clean_word(word) not in real_words:
                            print(word)
        except (
            IndexError,
            FileNotFoundError,
        ):
            print(f"Usage: python3 {sys.argv[0]} <file to check>")
