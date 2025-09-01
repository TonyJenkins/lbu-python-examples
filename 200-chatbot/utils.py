#!/usr/bin/env python3


def remove_punctuation(a_string):
    from string import punctuation

    return "".join([c for c in a_string if c not in punctuation])


if __name__ == "__main__":
    pass
