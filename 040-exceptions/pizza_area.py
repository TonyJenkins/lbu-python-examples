#!/usr/bin/env python3

from math import pi

if __name__ == "__main__":
    try:
        pizza_size = int(input("Enter the size of the pizza in inches: "))
        number_of_pizzas = int(input("Enter the number of pizzas:            "))
    except ValueError:
        print("Error! Numeric value needed.")
    else:
        if pizza_size in [9, 11, 13]:
            if number_of_pizzas > 0:
                pizza_area = pi * (pizza_size / 2) ** 2
                total_area = pizza_area * number_of_pizzas

                print(
                    f"A {pizza_size}-inch pizza has an area of {pizza_area:.2f} square inches."
                )
                print(
                    f"So in total you have a total pizza area of {total_area:.2f} square inches."
                )
            else:
                print("You have no pizzas! Please try again.")
        else:
            print(
                "You have non-standard pizzas! Please try again with a 9, 11, or 13-inch pizza."
            )
