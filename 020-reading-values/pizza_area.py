#!/usr/bin/env python3

from math import pi

if __name__ == "__main__":
    pizza_size = int(input("Enter the size of the pizza in inches: "))
    number_of_pizzas = int(input("Enter the number of pizzas:            "))

    pizza_area = pi * (pizza_size / 2) ** 2
    total_area = pizza_area * number_of_pizzas

    print(f"A {pizza_size}-inch pizza has an area of {pizza_area:.2f} square inches.")
    print(f"So in total you have a total pizza area of {total_area:.2f} square inches.")
