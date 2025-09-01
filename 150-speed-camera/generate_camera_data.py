#!/usr/bin/env python3

from random import choices, randint, uniform

from conf import SPEED_LIMITS, VEHICLE_TYPES


MAX_VEHICLES = 256
MIN_VEHICLES = 128

PERCENT_BUSES = 10
PERCENT_HGV = 15
PERCENT_VAN = 25
PERCENT_CAR = 50


def generate_random_vehicle_type():
    return choices(VEHICLE_TYPES, weights=(50, 20, 10, 20), k=1)[0]


def generate_random_speed(vehicle_type):
    match vehicle_type:
        case "C":
            return int(uniform(SPEED_LIMITS["C"] * 0.5, SPEED_LIMITS["C"] * 1.2))
        case "V":
            return int(uniform(SPEED_LIMITS["V"] * 0.5, SPEED_LIMITS["V"] * 1.2))
        case "B":
            return int(uniform(SPEED_LIMITS["B"] * 0.5, SPEED_LIMITS["B"] * 1.2))
        case "H":
            return int(uniform(SPEED_LIMITS["H"] * 0.5, SPEED_LIMITS["H"] * 1.2))
        case _:
            return None


def random_camera_line():
    vehicle_type = generate_random_vehicle_type()
    vehicle_speed = round(generate_random_speed(vehicle_type))

    return f"{vehicle_speed}{vehicle_type}"


def make_a_camera_file(file_name="camera_data.txt"):
    with open("camera_data.txt", "w") as speed_file:
        for count in range(randint(MIN_VEHICLES, MAX_VEHICLES)):
            speed_file.write(random_camera_line() + "\n")

        speed_file.write("OFF")


if __name__ == "__main__":
    make_a_camera_file()
