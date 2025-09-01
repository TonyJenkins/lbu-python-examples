#!/usr/bin/env python3

from random import random, randint
import sys


CAT_FILE = "cat_shelter.txt"
START_TIME = 640
END_TIME = 1260


def chance_of_cat_event():
    return random() > 0.9


def chance_it_is_our_cat():
    return random() > 0.8


def random_cat_event_duration():
    return randint(1, 10) * 5


def make_a_cat_file(file_name=CAT_FILE):
    time = START_TIME

    with open(CAT_FILE, "w") as cat_file:
        while time <= END_TIME:
            if chance_of_cat_event():
                if chance_it_is_our_cat():
                    duration_of_cat_event = random_cat_event_duration()
                    our_cat_or_their_cat = "OURS"
                else:
                    duration_of_cat_event = 1
                    our_cat_or_their_cat = "THEIRS"
                cat_file.write(
                    f"{our_cat_or_their_cat},{time},{time + duration_of_cat_event}\n"
                )

                time += duration_of_cat_event + 1
            else:
                time += 1

        cat_file.write("END")


if __name__ == "__main__":
    try:
        make_a_cat_file(sys.argv[1])
    except (
        IndexError,
        FileNotFoundError,
    ):
        make_a_cat_file()
