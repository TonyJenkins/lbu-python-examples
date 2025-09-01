#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        number_of_friends = int(input("How many friends do you have? "))
    except ValueError:
        print("Error! Integer value needed!")
    else:
        try:
            number_of_sweets = int(input("How many sweets do you have?  "))
        except ValueError:
            print("Error! Integer value needed!")
        else:
            try:
                if number_of_sweets < 0:
                    print("You cannot have a negative number of sweets!")
                else:
                    sweets_each = number_of_sweets // number_of_friends
                    left_over = number_of_sweets % number_of_friends

                    print(
                        f'With {number_of_friends} friend{"s" if number_of_friends != 1 else ""}, '
                        f'and {number_of_sweets} sweet{"s" if number_of_sweets != 1 else ""}, '
                        f'everyone gets {sweets_each} sweet{"s" if sweets_each != 1 else ""}, '
                        f"and there will be {left_over} left over."
                    )
            except ZeroDivisionError:
                print("You have no friends to share with. How sad.")
