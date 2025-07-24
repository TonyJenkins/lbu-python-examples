#!/usr/bin/env python3

from random import shuffle

from scrabble_exception import ScrabbleError


class Bag:

    frequency = {
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

    def __init__(self):
        self.letters = []
        for letter, count in self.frequency.items():
            self.letters.extend([letter] * count)

    def shake(self):
        shuffle(self.letters)

    def draw(self, n=1):
        if n > len(self.letters):
            return self.letters
        elif n <= 0:
            raise ScrabbleError("cannot deal that number of tiles")
        elif n > 1:
            result = self.letters[:n]
            self.letters = self.letters[n:]
            return result
        else:
            return self.letters.pop()

    def show(self):
        return ",".join(self.letters)

    def __len__(self):
        return len(self.letters)

    def __str__(self):
        return self.show()


if __name__ == "__main__":
    a_bag = Bag()
    print(a_bag)
    print()

    a_bag.shake()
    print(a_bag)
    print()

    for _ in range(4):
        a_bag.draw(7)
        print(a_bag)
        print()
