#!/usr/bin/env python3


def get_max_and_min_values(a_list):
    return max(a_list), min(a_list)


if __name__ == "__main__":
    for test_list in [
        [
            1,
            2,
            3,
            4,
            5,
        ],
        [
            5,
            4,
            3,
            2,
            1,
        ],
        [
            "cheese",
            "bacon",
            "eggs",
            "radish",
        ],
    ]:
        max_value, min_value = get_max_and_min_values(test_list)
        print(f"{test_list} : Max -> {max_value}, Min -> {min_value}")
