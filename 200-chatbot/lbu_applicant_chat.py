#!/usr/bin/env python3

import json
from random import choice

from log_utils import generate_log_file_name_from_time
from print_utils import banner_print
from utils import remove_punctuation


SETTINGS_FILE = "settings.json"


def check_settings_file():
    try:
        json.load(open(SETTINGS_FILE, "r"))["ExitWords"]
    except FileNotFoundError:
        raise FileNotFoundError("Settings file not found.")
    except json.decoder.JSONDecodeError:
        raise RuntimeError("Settings file is not a valid JSON file.")


def start_log_file(logfile):
    write_to_log(logfile, "SYSTEM", "Chat Started")


def log_users(logfile, user_name, agent_name):
    write_to_log(logfile, "SYSTEM", f"User identified as {user_name}")
    write_to_log(logfile, "SYSTEM", f"Agent identified as {agent_name}")


def write_to_log(logfile, actor, message):
    from datetime import datetime

    with open(logfile, "a") as log:
        log.write(f'{datetime.now().strftime("%H:%M")} --> {actor:<18}: {message}\n')


def get_words_from_question(the_question):
    return remove_punctuation(the_question).lower().split()


def get_user_name():
    while True:
        name = input("How shall we call you? ")

        if name:
            return name.strip().title()
        else:
            print("You must enter your name.")


def generate_agent_name():
    possible_names = json.load(open(SETTINGS_FILE, "r"))["OperatorNames"]

    return choice(possible_names)


def user_wants_to_exit(the_question):
    exit_words = json.load(open(SETTINGS_FILE, "r"))["ExitWords"]
    the_question = remove_punctuation(the_question)

    return any(word == the_question for word in exit_words)


def generate_response(the_question, name):
    responses = json.load(open(SETTINGS_FILE, "r"))["Responses"][0]

    question_words = get_words_from_question(the_question)

    for keyword in responses.keys():
        if keyword in question_words:
            return responses[keyword].replace("{name}", name)

    return generate_random_response(name)


def generate_random_response(name):
    possible_answers = json.load(open(SETTINGS_FILE, "r"))["DefaultAnswers"]

    random_answer = choice(possible_answers)

    return random_answer.replace("{name}", name)


def print_friendly_greeting(user_name, agent_name):
    banner_print("Welcome to LBU Applicant Chat!")
    print(f"Greetings, {user_name}. I am {agent_name}. How may I serve you? ")


def respond_to_questions(user_name, agent_name, logfile):
    while True:
        question = input("--> ")

        if question:
            if user_wants_to_exit(question):
                break

            write_to_log(logfile, f"User: {user_name}", question)

            response = generate_response(question, user_name)

            print(response)
            write_to_log(logfile, f"Agent: {agent_name}", response)


def say_farewell(user_name, logfile):
    banner_print(f"Thanks for using LBU Chat, {user_name}!")
    write_to_log(logfile, "SYSTEM", "Chat Ended")

    banner_print(f'A log has been written to "{logfile}".')


def run_chatbot():
    logfile = generate_log_file_name_from_time()
    start_log_file(logfile)

    user_name, agent_name = get_user_name(), generate_agent_name()
    log_users(logfile, user_name, agent_name)

    print_friendly_greeting(user_name, agent_name)
    respond_to_questions(user_name, agent_name, logfile)
    say_farewell(user_name, logfile)


def be_the_lbu_chatbot():
    try:
        check_settings_file()
    except FileNotFoundError:
        print("ERROR: Settings file not found. Exiting...")
    except RuntimeError:
        print("ERROR: Cannot start, Most likely a JSON problem in Settings. Exiting...")
    else:
        run_chatbot()


if __name__ == "__main__":
    be_the_lbu_chatbot()
