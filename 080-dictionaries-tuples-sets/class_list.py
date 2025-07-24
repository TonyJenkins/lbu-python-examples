#!/usr/bin/env python3


def add_student_mark(marks_so_far):
    print()

    name = input("Enter student name: ").lower()
    grade = int(input("Enter grade:        "))

    if name in marks_so_far:
        marks_so_far[name].append(grade)
    else:
        marks_so_far[name] = [
            grade,
        ]

    return marks_so_far


def generate_averages(all_marks):
    from statistics import mean

    averages = []

    for student in all_marks.keys():
        averages.append((student, mean(all_marks[student])))

    return averages


def print_final_list(unsorted_average_list):
    averages = unsorted_average_list.copy()

    averages.sort(key=lambda record: record[1], reverse=True)

    print()
    for student, average in averages:
        print(f"{student.title():12} - {average:.2f}")

    print()


def user_wants_to_end():
    again = input("Enter another (y/n)? ").lower()

    return again[0] == "n"


if __name__ == "__main__":
    raw_marks = {}

    while True:
        add_student_mark(raw_marks)

        if user_wants_to_end():
            break

    average_marks = generate_averages(raw_marks)
    print_final_list(average_marks)
