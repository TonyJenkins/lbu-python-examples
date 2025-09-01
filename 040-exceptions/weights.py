#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        kgs = float(input("Enter the weight in Kilograms: "))
    except ValueError:
        print("Error! Numeric value needed.")
    else:
        if kgs >= 0.0:
            stones = kgs / 6.34

            print(f"{kgs:.1f}Kg is equivalent to {stones:.1f} Stone.")
        else:
            print("You cannot have a negative weight.")
            print("Please try again with a positive value.")
