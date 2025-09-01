#!/usr/bin/env python3

from math import pi

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    else:
        if radius <= 0:
            print("Radius must be a positive number.")
        else:
            print(f"Calculating properties for a circle with radius: {radius}")
            circumference = 2 * pi * radius
            area = pi * (radius**2)

            print(f"Circumference: {circumference:.2f}")
            print(f"Area:          {area:.2f}")
