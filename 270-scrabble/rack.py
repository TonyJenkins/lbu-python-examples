#!/usr/bin/env python3

from random import shuffle

from bag import Bag
from scrabble_exception import ScrabbleError
from scrabble import possible_words_from_rack, word_score


class Rack:

    def __init__(self):

        self.bag = Bag()
        self.bag.shake()

        self.letters = self.bag.draw(7)

    def show(self):
        return "-".join(self.letters)

    def sort(self):
        self.letters.sort()

    def shuffle(self):
        shuffle(self.letters)

    def use(self, letters_to_use):
        temp_rack = self.letters[:]

        for letter in letters_to_use:
            try:
                temp_rack.remove(letter)
            except ValueError:
                raise ScrabbleError("letter not available in rack")

        for letter in letters_to_use:
            self.letters.remove(letter)

        new_letters = self.bag.draw(len(letters_to_use))
        for tile in new_letters:
            self.letters.append(tile)

    def best_word(self):
        possible_words = possible_words_from_rack(self.letters)

        best_score = 0
        best_word = ""

        for word in possible_words:
            if word_score(word) > best_score:
                best_score, best_word = word_score(word), word

        return best_word, best_score

    def __str__(self):
        return self.show()

    def __len__(self):
        return len(self.letters)


if __name__ == "__main__":
    rack = Rack()
    print(rack)

    best_word, best_score = rack.best_word()
    print(f"Play {best_word} to score {best_score}!")

    rack.use(best_word)
    print(rack)
