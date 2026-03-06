#!/usr/bin/env python3

from random import randint

LOWER_LIMIT = 17
UPPER_LIMIT = 29
DELTA_LIMIT = 5


def die_roll(sides=6):
    return randint(1, sides)


def play_a_round(current_score, current_turns):
    roll = die_roll(6)

    return current_score + roll, roll, current_turns + 1


def generate_target(lower=LOWER_LIMIT, upper=UPPER_LIMIT):
    return randint(lower, upper)


def within_limits(score, target, delta):
    return abs(score - target) <= delta


def print_game_status(target, score, turns, roll=None):
    if not roll:
        print(f"({turns}) The target is {target}. Your current score is: {score}")
    else:
        print(f"({turns}) The target is {target}. You rolled {roll}. Your score is now {score}")


def show_end_game(target, score, final_turns, delta=DELTA_LIMIT):
    print()
    print(f"The target was {target}.")
    print(f"You had {final_turns} roll{'s' if final_turns > 1 else ''}.")
    print(f"Your final score is: {score}.")

    if within_limits(score, target, delta):
        print(f"So your final score was {abs(target - score)}.")
    else:
        print("Sadly, you finished too far from the target.")


def play_the_game():
    target = generate_target()
    total_score = 0
    turns = 0

    print_game_status(target, total_score, turns)

    while True:
        carry_on = input("Roll the die? (y/n): ").strip().lower()
        if carry_on == "y":
            total_score, roll, turns = play_a_round(total_score, turns)
            print_game_status(target, total_score, turns, roll)
        elif carry_on == "n":
            break
        else:
            print('Please respond with "y" or "n"')

    show_end_game(target, total_score, turns)


if __name__ == "__main__":
    play_the_game()
