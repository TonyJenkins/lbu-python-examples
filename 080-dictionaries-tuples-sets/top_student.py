#!/usr/bin/env python3


def top_student(records):
    from operator import itemgetter

    records.sort(key=itemgetter(2), reverse=True)

    return records[0]


if __name__ == "__main__":
    STUDENTS = [
        ("Ronald", "Jones", 66.5),
        ("Barbara", "Brown", 70),
        ("Craig", "Cheeseman", 80.5),
        ("Doris", "Johnson", 55),
    ]

    first_name, surname, score = top_student(STUDENTS)
    print(f"Top Student is {first_name} {surname} with score {score}.")
