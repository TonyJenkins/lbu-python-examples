#!/usr/bin/env python3

from rack import Rack


def print_end_game(words_played, letters_left):
    words_played.sort(key=lambda x: x[1], reverse=True)

    print()
    print(f"{len(words_played)} words played.")
    print(f"{sum([words[1] for words in words_played])} total score.")
    print()
    print(f'"{letters_left}" not played.')
    print()
    print("Best Five Words:")
    for word in words_played[:5]:
        print(f"{word[0]} ({word[1]})")


def play_solo_scrabble():
    the_letters = Rack()

    words_played = []

    while True:
        print(f"Current Rack: {the_letters}")

        best_word, best_score = the_letters.best_word()
        print(f"Play {best_word} to score {best_score}!")

        words_played.append(
            [best_word, best_score],
        )

        the_letters.use(best_word)

        if len(the_letters) < 7:
            break

    print_end_game(words_played, the_letters)


if __name__ == "__main__":
    play_solo_scrabble()
