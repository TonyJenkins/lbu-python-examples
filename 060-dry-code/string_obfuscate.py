#!/usr/bin/env python3


from random import choice, randint
from string import ascii_letters as letters


if __name__ == '__main__':
    message = input('Enter a message to obfuscate: ')

    noise_length = randint(1, 5)
    hidden_message = ''
    
    for c in message:
        hidden_message += c
        for _ in range(noise_length):
            hidden_message += choice(letters)

    print(f'Obfuscated message: {hidden_message}')
