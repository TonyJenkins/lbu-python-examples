#!/usr/bin/env python3

if __name__ == "__main__":
    celsius = float(input("Enter the temperature in Celsius: "))

    fahrenheit = 9 / 5 * celsius + 32

    print(f"{celsius:.1f}C is equivalent to {fahrenheit:.1f}F.")
