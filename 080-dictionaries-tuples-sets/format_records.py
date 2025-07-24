#!/usr/bin/env python3


def format_and_sort_records(records):
    from operator import itemgetter

    output = []

    for record in sorted(records, key=itemgetter(2), reverse=True):
        first_name, surname, score = record
        output.append(f"{surname:10} {first_name:10} {score:5.2f}")

    return "\n".join(output)


if __name__ == "__main__":
    STUDENTS = [
        ("Ronald", "Jones", 66.5),
        ("Barbara", "Brown", 70),
        ("Craig", "Cheeseman", 80.5),
        ("Doris", "Johnson", 55),
    ]

    print(format_and_sort_records(STUDENTS))
