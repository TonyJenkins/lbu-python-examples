#!/usr/vbin/env python3

import requests

from useless_exception import UselessError


USELESS_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"


def get_useless_json(useless_url=USELESS_URL):
    try:
        response = requests.get(useless_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise UselessError("Useless URL problem")
    except requests.exceptions.RequestException:
        raise UselessError("Network problems")


def get_a_useless_fact():
    json_fact = get_useless_json()

    return json_fact["text"]


def print_a_useless_fact():
    print(get_a_useless_fact())


if __name__ == "__main__":
    try:
        print_a_useless_fact()
    except (
        UselessError,
        requests.exceptions.RequestException,
    ) as e:
        print(f"Failed to get a useless fact. How ironic. ({e.message}).")
