#!/usr/bin/env python3

import names
from random import random, randint
from xkcdpass import xkcd_password as xp


from passwd_utils import PASSWORD_FILE, add_user_to_file


NUMBER_OF_USERS = 32


def generate_full_name():
    number_of_forenames = randint(1, 3)
    gender = "male" if random() > 0.5 else "female"

    name = " ".join(
        [names.get_first_name(gender) for count in range(number_of_forenames)]
    )
    name += " " + names.get_last_name()

    return name


def lowercase_initials(full_name):
    return "".join([c for c in full_name if c.isupper()]).lower()


def generate_username(full_name):
    first_name, last_name = full_name.split(" ")[0], full_name.split(" ")[-1]

    if random() < 0.33:
        return lowercase_initials(full_name)
    elif random() < 0.66:
        return last_name.lower()
    else:
        return first_name.lower()


def generate_password():
    wordfile = xp.locate_wordfile()
    words = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)

    return xp.generate_xkcdpassword(words, 3, delimiter="")


def generate_a_dummy_password_file(passwd_txt=PASSWORD_FILE):
    with open(passwd_txt, "w") as of:
        for line in range(NUMBER_OF_USERS):
            full_name = generate_full_name()
            username = generate_username(full_name)
            password = generate_password()
            try:
                add_user_to_file((username, full_name, password))
            except:
                pass


if __name__ == "__main__":
    generate_a_dummy_password_file()
