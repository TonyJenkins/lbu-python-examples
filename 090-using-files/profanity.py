#!/usr/bin/env python3


import sys
import nltk


REDACT_FILE = 'redact.txt'
WORD_CONTRACTION_ENDINGS = ['s', 'nt']


def load_redacted_words(bad_words=REDACT_FILE):
    with open(bad_words, 'r') as f:
        return f.read().splitlines()


def redact_word(w, words_to_redact):
    if w in words_to_redact:
        return '*' * len(w)
    else:
        return w

def is_a_word(w):
    for c in w:
        if not c.isalpha() and c != '-':
            return False

    return True


if __name__ == '__main__':

    nltk.download('punkt_tab')

    redactions = load_redacted_words()

    try:
        with open(sys.argv[1]) as infile, open(sys.argv[2], 'w') as outfile:
            for line in infile:
                for word in nltk.word_tokenize(line):
                    redacted_word = redact_word(word, redactions)
                    if is_a_word(word) and word not in WORD_CONTRACTION_ENDINGS:
                        outfile.write(' ' + redacted_word)
                    else:
                        outfile.write(redacted_word)
                outfile.write('\n')

    except IndexError:
        print(f'{sys.argv[0]}: Usage: python3 {sys.argv[0]} <infile> <outfile>')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"')
