#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        distance = float(input("Enter the distance in miles: "))
        time = float(input("Enter the time in minutes:   "))
    except ValueError:
        print("Error! Numeric value needed.")
    else:
        if distance > 0 and time > 0:
            mph = distance / (time / 60)

            if mph < 75:
                print(
                    f"Travelling {distance} miles in {time} minutes is equivalent to {mph:.2f} mph."
                )
            else:
                print(
                    f"Travelling {distance} miles in {time} minutes is equivalent to {mph:.2f} mph, which is way too fast!"
                )
        else:
            print("Distance and time must be greater than zero! Please try again.")
