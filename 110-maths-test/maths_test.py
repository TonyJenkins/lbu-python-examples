#!/usr/bin/env python3


from random import choice, randint
import conf


def generate_random_term(max_value = conf.MAX_VALUE):
    return randint(0, max_value)


def get_answer(question_text):
    while True:
        try:
            answer_entered = int(input(question_text))
            return answer_entered
        except ValueError:
            print('Answer must be an integer!')


def do_addition_question():
    term_1 = generate_random_term()
    term_2 = generate_random_term()

    answer = get_answer(f'{term_1} + {term_2} = ')

    return answer == term_1 + term_2


def do_subtraction_question(avoid_negatives = conf.AVOID_NEGATIVE_RESULTS):
    term_1 = generate_random_term()
    term_2 = generate_random_term()

    if avoid_negatives:
        if term_1 < term_2:
            term_1, term_2 = term_2, term_1

    answer = get_answer(f'{term_1} - {term_2} = ')

    return answer == term_1 - term_2


def do_multiplication_question():
    pass


def do_division_question():
    pass



def setup_test():
    question_types = []

    if conf.INCLUDE_ADDITION:
        question_types.append('+')
    if conf.INCLUDE_SUBTRACTION:
        question_types.append('-')
    if conf.INCLUDE_MULTIPLICATION:
        question_types.append('*')
    if conf.INCLUDE_DIVISION:
        question_types.append('/')

    if not question_types:
        raise ValueError('No questions types configured')
    
    return question_types


def do_the_maths_test(question_types_configured):

    correct_answers = 0

    for question in range(conf.QUESTIONS):
        this_question = choice(question_types_configured)

        match this_question:
            case '+':
                result = do_addition_question()
            case '-':
                result = do_subtraction_question()
            case '*':
                result = do_multiplication_question()
            case '/':
                result = do_division_question()

        correct_answers += 1 if result else 0

    print(correct_answers)


if __name__ == '__main__':
    question_types = setup_test()
    do_the_maths_test(question_types)

