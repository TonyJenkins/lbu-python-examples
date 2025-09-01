#!/usr/bin/env python3

from random import choice, randint
from string import ascii_letters as letters


def obfuscate_message(message, noise_length):
    hidden_message = ""
    for c in message:
        hidden_message += c
        for _ in range(noise_length):
            hidden_message += choice(letters)
    return hidden_message


def do_some_obfuscation():
    noise_length = randint(1, 5)
    message = input("Enter a message to obfuscate: ")
    print(obfuscate_message(message, noise_length))


if __name__ == "__main__":
    do_some_obfuscation()
