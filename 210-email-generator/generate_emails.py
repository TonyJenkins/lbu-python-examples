#!/usr/bin/env python3

from random import randint
import sys


DOMAIN = "leedsbeckett.ac.uk"


def line_split(infile_line):
    return infile_line[:8], infile_line[8:]


def find_capitals(s):
    return "".join([c if c.isupper() else "" for c in s])


def to_initials(initials):
    return ".".join(initials.lower())


def four_random_digits():
    rd = ""

    for _ in range(4):
        rd += str(randint(0, 9))

    return rd


def clean_surname(surname):
    surname = surname.lower().strip()

    return "".join([c if c.isalpha() else "" for c in surname])


def build_email(full_name):
    try:
        surname, forenames = full_name.split(",")
    except ValueError:
        surname, forenames = full_name, None

    surname = clean_surname(surname)
    if forenames:
        initials = to_initials(find_capitals(forenames))
        return f"{initials}.{surname}{four_random_digits()}@{DOMAIN}".lower()
    else:
        return f"{surname}{four_random_digits()}@{DOMAIN}".lower()


def generate_the_file_of_emails(file_with_list_of_users, output_file_name="emails.txt"):
    with open(file_with_list_of_users, "r") as user_file, open(
        output_file_name, "w"
    ) as email_file:
        for user_line in user_file.readlines():
            user_id, name = line_split(user_line)

            email_file.write(f"{user_id} {build_email(name)}\n")


if __name__ == "__main__":

    try:
        generate_the_file_of_emails(sys.argv[1])

    except FileNotFoundError:
        print(f"{sys.argv[0]}: File not found")
    except IndexError:
        print(f"{sys.argv[0]}: Missing CLA")
