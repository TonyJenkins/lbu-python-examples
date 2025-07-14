#!/usr/bin/env python3

if __name__ == '__main__':

    possible_password = input('Enter new password: ')

    has_uppercase = haslowercase = has_digit = has_special = False

    for character in possible_password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_uppercase and has_lowercase and has_digit and has_special:
        print('Password is complex!')
    else:
        print('Password might be easy to guess. Change it!')
        