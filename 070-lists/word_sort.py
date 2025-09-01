#!/usr/bin/env python3


def sort_string(s):
    from word_clean import clean_string

    return "".join([c for c in sorted(clean_string(s))])


if __name__ == "__main__":
    for test_string in ["zyxabcde", "ghia***bcd((e))", "&&&&", "PQRA123"]:
        print(f"'{test_string}' -> '{sort_string(test_string)}'")
