#!/usr/bin/env python3

import sys

from conf import DRIVER_FILE, DEFAULT_LAP_TIMES_FILE
from driver import Driver


def create_driver_list(driver_file=DRIVER_FILE):
    driver_list = []

    with open(driver_file, "r") as df:
        for driver in df:
            number, code, name, team = driver.strip().split(",")
            driver_list.append(Driver(number, code, name, team))

    return driver_list


def record_a_lap(drivers, code, lap_time):
    for driver in drivers:
        if driver.code == code:
            driver.record_lap_time(lap_time)
            break


def process_lap_times(drivers, lap_times_file=DEFAULT_LAP_TIMES_FILE):
    with open(lap_times_file, "r") as lap_times:
        for lap_time in lap_times:
            code, time = lap_time.strip().split(",")
            record_a_lap(drivers, code, float(time))


def print_leaderboard(drivers):
    import tabulate

    drivers.sort()

    leaderboard = [
        ("#", "Time", "", "Driver", "Team"),
    ]

    for driver in drivers:
        leaderboard.append(
            (
                driver.number,
                driver.fastest_lap_time,
                driver.code,
                driver.name,
                driver.team,
            )
        )

    print(
        tabulate.tabulate(
            leaderboard, tablefmt="fancy_grid", floatfmt=".3f", headers="firstrow"
        )
    )


def run_qualifying(lap_times_file=DEFAULT_LAP_TIMES_FILE):
    drivers = create_driver_list()
    process_lap_times(drivers, lap_times_file)
    print_leaderboard(drivers)


if __name__ == "__main__":
    try:
        run_qualifying(sys.argv[1])
    except IndexError:
        run_qualifying()
    except FileNotFoundError:
        print(f'Cannot open "{sys.argv[1]}".', file=sys.stderr)
