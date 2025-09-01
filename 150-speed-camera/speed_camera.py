#!/usr/bin/env python3

import sys

from conf import SPEED_LIMITS, VEHICLE_TYPES


def initialise_speed_lists():
    return {vehicle_type: [] for vehicle_type in VEHICLE_TYPES}


def parse_speed_line(speed_line):
    speed_line = speed_line.strip()

    return speed_line[-1], int(speed_line[:-1])


def analyse_the_camera_file(camera_file):
    speeds = initialise_speed_lists()

    with open(camera_file, "r") as cf:
        for speed_line in cf:
            if speed_line != "OFF":
                vehicle_type, speed = parse_speed_line(speed_line)
                speeds[vehicle_type].append(speed)

    analyse_and_print_results(speeds)


def count_total_vehicles(speeds):
    return sum([len(speeds[c]) for c in VEHICLE_TYPES])


def get_vehicle_type_percentage(speeds, vehicle_type):
    return len(speeds[vehicle_type]) / count_total_vehicles(speeds) * 100


def count_vehicle_type(speeds, vehicle_type):
    return len(speeds[vehicle_type])


def get_vehicle_type_average_speed(speeds, vehicle_type):
    from statistics import mean

    return mean(speeds[vehicle_type])


def count_vehicle_type_speeders(speeds, vehicle_type, limit):
    return len([s for s in speeds[vehicle_type] if s > limit])


def get_total_speeder_percent(speeds):
    total_vehicles = count_total_vehicles(speeds)
    total_speeders = (
        count_vehicle_type_speeders(speeds, "C", SPEED_LIMITS["C"])
        + count_vehicle_type_speeders(speeds, "V", SPEED_LIMITS["V"])
        + count_vehicle_type_speeders(speeds, "B", SPEED_LIMITS["B"])
        + count_vehicle_type_speeders(speeds, "H", SPEED_LIMITS["H"])
    )

    return total_speeders / total_vehicles * 100


def print_analysis_header():
    print()
    print("Speed Camera Summary")
    print("====================")
    print()


def analyse_and_print_results(speeds):
    print_analysis_header()
    print(f"Total Vehicles Seen: {count_total_vehicles(speeds)}")
    print()
    print(f"Percentage Cars:  {get_vehicle_type_percentage(speeds, 'C'):6.2f}%")
    print(f"Percentage Vans:  {get_vehicle_type_percentage(speeds, 'V'):6.2f}%")
    print(f"Percentage Buses: {get_vehicle_type_percentage(speeds, 'B'):6.2f}%")
    print(f"Percentage HGVs:  {get_vehicle_type_percentage(speeds, 'H'):6.2f}%")
    print()
    print(f"Average Car Speed: {get_vehicle_type_average_speed(speeds, 'C'):6.2f} MPH")
    print(f"Average Van Speed: {get_vehicle_type_average_speed(speeds, 'V'):6.2f} MPH")
    print(f"Average Bus Speed: {get_vehicle_type_average_speed(speeds, 'B'):6.2f} MPH")
    print(f"Average HGV Speed: {get_vehicle_type_average_speed(speeds, 'H'):6.2f} MPH")
    print()
    print(
        f"Speeding Cars:  {count_vehicle_type_speeders(speeds, 'C', SPEED_LIMITS['C'])}"
        f" of {count_vehicle_type(speeds, 'C')}"
    )
    print(
        f"Speeding Vans:  {count_vehicle_type_speeders(speeds, 'V', SPEED_LIMITS['V'])}"
        f" of {count_vehicle_type(speeds, 'V')}"
    )
    print(
        f"Speeding Buses: {count_vehicle_type_speeders(speeds, 'B', SPEED_LIMITS['B'])}"
        f" of {count_vehicle_type(speeds, 'B')}"
    )
    print(
        f"Speeding HGVs:  {count_vehicle_type_speeders(speeds, 'H', SPEED_LIMITS['H'])}"
        f" of {count_vehicle_type(speeds, 'H')}"
    )
    print()
    print(f"Overall percentage of speeders: {get_total_speeder_percent(speeds):.2f}%")


if __name__ == "__main__":
    analyse_the_camera_file("camera_data.txt")
