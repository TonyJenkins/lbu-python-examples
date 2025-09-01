#!/usr/bin/env python3


MENU = {
    "tea": 1.95,
    "sandwich": 4.95,
    "apple": 0.75,
    "coffee": 2.30,
    "lemonade": 2.50,
    "chips": 3.00,
    "toastie": 3.95,
}


def add_up_the_bill():
    total = 0

    while True:
        item = input("Enter an Ordered Item: ").strip()

        if not item:
            break

        if item in MENU:
            total += MENU[item]
            print(
                f"Adding £{MENU[item]:.2f} to the bill for {item.title()}, total is £{total:.2f}."
            )
        else:
            print(f"We are right out of {item.title()} today, unfortunately.")

    return total


if __name__ == "__main__":
    print(f"Your total is £{add_up_the_bill():.2f}.")
