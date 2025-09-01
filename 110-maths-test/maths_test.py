#!/usr/bin/env python3


from random import choice, randint

import conf
from maths_test_exception import MathsTestConfigError


def generate_random_term(max_value=conf.MAX_VALUE):
    return randint(0, max_value)


def get_answer(question_number, term_1, term_2, operation):
    while True:
        try:
            prompt_text = (
                f"Question {question_number + 1:2}: {term_1} {operation} {term_2} = "
            )
            return int(input(prompt_text))
        except ValueError:
            print("Answer must be an integer!")


def do_addition_question(question_number):
    term_1 = generate_random_term()
    term_2 = generate_random_term()

    answer = get_answer(question_number, term_1, term_2, "+")

    return answer == term_1 + term_2


def do_subtraction_question(
    question_number, avoid_negatives=conf.AVOID_NEGATIVE_RESULTS
):
    term_1 = generate_random_term()
    term_2 = generate_random_term()

    if avoid_negatives:
        if term_1 < term_2:
            term_1, term_2 = term_2, term_1

    answer = get_answer(question_number, term_1, term_2, "-")

    return answer == term_1 - term_2


def do_multiplication_question(question_number):
    term_1 = generate_random_term()
    term_2 = generate_random_term()

    answer = get_answer(question_number, term_1, term_2, "x")

    return answer == term_1 * term_2


def do_division_question(question_number):
    term_1 = generate_random_term()
    term_2 = randint(1, conf.MAX_DIVISION_FACTOR)

    answer = get_answer(question_number, term_1, term_2, "/")

    return answer == term_1


def setup_test():
    question_types = []

    if conf.INCLUDE_ADDITION:
        question_types.append("+")
    if conf.INCLUDE_SUBTRACTION:
        question_types.append("-")
    if conf.INCLUDE_MULTIPLICATION:
        question_types.append("*")
    if conf.INCLUDE_DIVISION:
        question_types.append("/")

    if not question_types:
        raise MathsTestConfigError("No question types configured")

    return question_types


def print_results(number_correct, number_answered):
    print()
    print("Test Complete!")
    print()
    print(f"You scored {number_correct / number_answered * 100:.2f}%.")


def do_the_maths_test(question_types_configured):

    correct_answers = 0

    for question_number in range(conf.QUESTIONS):
        this_question = choice(question_types_configured)

        match this_question:
            case "+":
                result = do_addition_question(question_number)
            case "-":
                result = do_subtraction_question(question_number)
            case "*":
                result = do_multiplication_question(question_number)
            case "/":
                result = do_division_question(question_number)
            case _:
                result = None

        correct_answers += 1 if result else 0

    print_results(correct_answers, conf.QUESTIONS)


if __name__ == "__main__":
    try:
        question_types = setup_test()
        do_the_maths_test(question_types)
    except MathsTestConfigError:
        print(
            "Error: Problem in the config. Most likely, no question types configured."
        )
