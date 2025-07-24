#!/usr/bin/env python3

if __name__ == "__main__":
    number_of_eggs = 157

    boxes_of_twelve = number_of_eggs // 12
    boxes_of_six = (number_of_eggs % 12) // 6
    left_over = number_of_eggs - (boxes_of_twelve * 12 + boxes_of_six * 6)

    print(
        f"With {number_of_eggs} eggs, we can fill {boxes_of_twelve} boxes of twelve, "
        f"{boxes_of_six} boxes of six, and have {left_over} eggs left over."
    )
