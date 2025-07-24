#!/usr/bin/env python3


def find_most_common_letters(words):
    from collections import Counter

    counts = Counter(words)
    max_count = max(counts.values())

    return "".join(sorted([c for c in counts if counts[c] == max_count]))


if __name__ == "__main__":
    for word in ["cheese", "spam", "unicorn", "banana", "toot"]:
        print(f"{word}: {find_most_common_letters(word)}")
