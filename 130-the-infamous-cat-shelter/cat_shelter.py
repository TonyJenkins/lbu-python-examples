#!/usr/bin/env python3

from statistics import mean
import sys


def time_in_hours(total_minutes):
    hours = total_minutes // 60
    mins = total_minutes % 60

    hours_word = "Hour" if hours == 1 else "Hours"
    minutes_word = "Minute" if mins == 1 else "Minutes"

    if hours > 0:
        return f"{hours} {hours_word}, {mins} {minutes_word}"
    else:
        return f"{mins} {minutes_word}"


def print_results(time_list, other_cat_count):
    print()
    print("Log File Analysis")
    print("==================")
    print()
    print(f"Cat Visits: {len(time_list)}")
    print(f"Other Cats: {other_cat_count}")
    print()
    print(f"Total Time in House: {time_in_hours(sum(time_list))}")
    print()
    print(f"Average Visit Length: {time_in_hours(int(mean(time_list)))}")
    print(f"Longest Visit:        {time_in_hours(max(time_list))}")
    print(f"Shortest Visit:       {time_in_hours(min(time_list))}")
    print()


def analyse_the_cat_log(cata_log):
    times = []
    others = 0

    with open(sys.argv[1], "r") as cata_log:
        for cat_event in cata_log:
            if cat_event != "END":
                cat, start, end = cat_event.split(",")

                if cat == "OURS":
                    times.append(int(end) - int(start))
                else:
                    others += 1

    print_results(times, others)


if __name__ == "__main__":
    try:
        analyse_the_cat_log(sys.argv[1])
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}"!')
    except IndexError:
        print(f"{sys.argv[0]}: Missing command line argument.")
