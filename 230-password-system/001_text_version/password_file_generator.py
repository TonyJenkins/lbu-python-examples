#!/usr/bin/env python3

import names
from random import random, randint
from xkcdpass import xkcd_password as xp


from passwd_utils import PASSWORD_FILE, add_user_to_file


NUMBER_OF_USERS = 32


def generate_name():

    forenames = randint(1, 3)
    gender = 'male' if random() > 0.5 else 'female'

    name = ' '.join([names.get_first_name(gender) for count in range(forenames)])
    name += ' ' + names.get_last_name()

    return name


def initials(name):
    return ''.join([c for c in name if c.isupper()]).lower()


def generate_username(name):

    if random() < 0.33:
        return initials(name)
    elif random() < 0.66:
        return name.split(' ')[-1].lower()
    else:
        return name.split(' ')[0].lower()


def generate_password():

    wordfile = xp.locate_wordfile()
    words = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)

    return xp.generate_xkcdpassword(words, 3, delimiter='')


if __name__ == '__main__':

    with open(PASSWORD_FILE, 'w') as out:
        for line in range(NUMBER_OF_USERS):
            name = generate_name()
            username = generate_username(name)
            password = generate_password()
            try:
                add_user_to_file((username, name, password))
            except:
                pass
