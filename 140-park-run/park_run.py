#!/usr/bin/env python3


def time_as_string(seconds):
    mins = int(seconds // 60)
    secs = round(seconds % 60, 1)

    return f'{mins} minute{"" if mins == 1 else "s"}, {secs} second{"" if secs == 1 else "s"}'


def parse_time_record(line_from_the_stream):
    try:
        singlet_number, time = line_from_the_stream.split("::")

        if len(singlet_number) < 1:
            raise ValueError("Missing singlet number")

        return singlet_number, int(time)
    except ValueError:
        raise ValueError("Error in data. Probably cannot convert time")


def print_headers():
    print()
    print("Park Run Timer")
    print("~~~~~~~~~~~~~~")
    print()
    print("Let's go!")
    print()


def print_results(all_times, top_runner):
    from statistics import mean

    if all_times:
        print()
        print(f"Total Runners: {len(all_times)}")
        print(f"Average Time:  {time_as_string(mean(all_times))}")
        print(f"Fastest Time:  {time_as_string(min(all_times))}")
        print(f"Slowest Time:  {time_as_string(max(all_times))}")
        print()
        print(f"Best Time Here: Runner #{top_runner}")
        print()
    else:
        print("No data found. Nothing to do. What a pity.")


def process_the_park_run():
    times = []
    top_runner = ""

    while True:
        next_line = input("> ")

        if next_line == "END":
            print_results(times, top_runner)
            break
        else:
            try:
                runner, time = parse_time_record(next_line)

                if times:
                    top_runner = runner if time < min(times) else top_runner
                else:
                    top_runner = runner

                times.append(time)

            except ValueError:
                print("Error in data stream. Ignoring. Carry on.")


if __name__ == "__main__":
    process_the_park_run()
