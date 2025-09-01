#!/usr/bin/env python3

if __name__ == "__main__":
    celsius = float(input("Enter the temperature in Celsius: "))

    if celsius < -273.15:
        print("That is below absolute zero! Please enter a valid temperature.")
    elif celsius > 100:
        print("That is an extremely high temperature! Please enter a reasonable value.")
    elif celsius < -100:
        print("That is a very low temperature! Please enter a reasonable value.")
    else:
        fahrenheit = 9 / 5 * celsius + 32

        print(f"{celsius:.1f}C is equivalent to {fahrenheit:.1f}F.")
