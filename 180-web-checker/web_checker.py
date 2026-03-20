#!/usr/bin/env python3

import sys


from requests import get
from requests.exceptions import RequestException


def url_is_accessible(url):
    try:
        get(url)
        return True
    except RequestException:
        return False


def get_http_code(url):
    return get(url).status_code


def check_a_url(url):
    if url_is_accessible(url):
        return get_http_code(url)
    else:
        return None


def check_the_urls(list_of_urls):
    for url in list_of_urls:
        if not check_a_url(url):
            print(f"{url} is not accessible")
        else:
            print(f"{url} returns {get_http_code(url)}")


if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as f:
            urls = [url.strip() for url in f.readlines()]
            check_the_urls(urls)
    except IndexError:
        print("Missing argument")
        print(f"Usage: {sys.argv[0]} <urls.txt>")
    except FileNotFoundError:
        print("File not found")
        print(f"Usage: {sys.argv[0]} <urls.txt>")
