#!/usr/bin/env python3

import sys


def read_file(filename):
    with open(filename) as f:
        return f.read()


def clean_string(s):
    return "".join([c for c in s if c.isalpha() or c.isspace()])


def join_lines(s):
    return s.replace("\n", " ")


def build_word_list(string_of_words):
    return string_of_words.split()


def print_top_words(word_list):
    from collections import Counter

    word_frequencies = Counter(word_list)
    for word, frequency in sorted(
        word_frequencies.most_common(10), key=lambda x: x[1], reverse=True
    ):
        print(f"{word}: {frequency}")


def do_the_word_count():
    try:
        raw_file = read_file(sys.argv[1])
    except IndexError:
        print(f"{sys.argv[0]}: Usage: python3 word_count.py <file>")
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')
    else:
        clean_file = join_lines(clean_string(raw_file))
        word_list = build_word_list(clean_file)
        print_top_words(word_list)


if __name__ == "__main__":
    do_the_word_count()
