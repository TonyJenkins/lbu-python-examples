#!/usr/bin/env python3

from conf import DRIVER_FILE

MAX_LAPS = 60
MIN_LAPS = 30

MAX_LAP_TIME = 120
MIN_LAP_TIME = 110

TOP_TEAM = [
    "McLaren",
    "Ferrari",
]
MIDDLE_TEAM = [
    "Mercedes",
    "Red Bull",
    "Williams",
    "Kick Sauber",
]


OUTPUT_FILE = "lap_times.txt"


def get_drivers_from_file(driver_file=DRIVER_FILE):
    drivers = []

    with open(driver_file, "r") as df:
        for driver in df:
            _, short_code, __, team = driver.strip().split(",")
            drivers.append((short_code, team))

    return drivers


def generate_the_lap_times(driver_file=DRIVER_FILE, lap_file=OUTPUT_FILE):
    from random import randint, shuffle, uniform

    drivers = get_drivers_from_file(driver_file)

    lap_times = []

    for driver in drivers:
        code, team = driver
        for lap in range(randint(MIN_LAPS, MAX_LAPS)):
            if team in TOP_TEAM:
                min_lap_time = MIN_LAP_TIME - 1.5
                max_lap_time = MAX_LAP_TIME - 2
            elif team in MIDDLE_TEAM:
                min_lap_time = MIN_LAP_TIME - 1
                max_lap_time = MAX_LAP_TIME + 1
            else:
                min_lap_time = MIN_LAP_TIME
                max_lap_time = MAX_LAP_TIME + 2

            lap_times.append(f"{code},{uniform(min_lap_time, max_lap_time):.3f}")

    shuffle(lap_times)

    with open(OUTPUT_FILE, "w") as out:
        for lap_time in lap_times:
            out.write(lap_time + "\n")


if __name__ == "__main__":
    generate_the_lap_times()
