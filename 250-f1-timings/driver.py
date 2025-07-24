#!/usr/bin/env python3


class Driver:

    def __init__(self, number, code, name, team):
        self.number = number
        self.code = code
        self.name = name
        self.team = team

        self.practice_times = []

    @property
    def laps_run(self):
        return len(self.practice_times)

    @property
    def avg_lap_time(self):
        from statistics import mean

        if self.laps_run == 0:
            return 0.0
        else:
            return mean(self.practice_times)

    @property
    def fastest_lap_time(self):
        if self.laps_run == 0:
            return 0.0
        else:
            return min(self.practice_times)

    def record_lap_time(self, lap_time):
        self.practice_times.append(lap_time)

    def __lt__(self, other):
        return self.fastest_lap_time < other.fastest_lap_time


if __name__ == "__main__":
    pass
