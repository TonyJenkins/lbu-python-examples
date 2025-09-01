#!/usr/bin/env python3


def get_nato_letter(letter):
    nato_alphabet = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu",
    }
    try:
        return nato_alphabet[letter.upper()]
    except KeyError:
        return None


if __name__ == "__main__":
    message = input("Enter your message: ")

    for character in message:
        if get_nato_letter(character):
            print(get_nato_letter(character))
        else:
            print(character)
