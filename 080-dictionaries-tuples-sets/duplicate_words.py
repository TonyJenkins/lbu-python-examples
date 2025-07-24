#!/usr/bin/env python3


def clean_sentence(sentence):
    return "".join([c for c in sentence.lower().strip() if c.isalpha() or c == " "])


def find_duplicate_words(sentence):
    from collections import Counter

    counts = Counter(sentence.split())
    max_count = max(counts.values())

    return [c for c in counts if counts[c] == max_count]


if __name__ == "__main__":
    test_sentence = "The key of my aunt is key to the problem of my uncle."
    print(find_duplicate_words(clean_sentence(test_sentence)))
