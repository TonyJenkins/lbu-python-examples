#!/usr/bin/env python3


def leave_queue(current_queue):

    return current_queue.pop(0), current_queue


def join_queue(current_queue, new_entry):
    current_queue.append(new_entry)

    return current_queue


def clear_queue(current_queue):
    current_queue.clear()

    return current_queue


def print_queue(current_queue):
    if len(current_queue) == 0:
        print("Queue is empty.")
    else:
        for pos in range(len(current_queue)):
            print(f"{pos:3} {current_queue[pos]}")


if __name__ == "__main__":
    queue = []

    join_queue(queue, "Arnold")
    join_queue(queue, "Bertha")
    join_queue(queue, "Colin")
    join_queue(queue, "Debra")

    print_queue(queue)
    print()

    leaver, queue = leave_queue(queue)
    print(f"{leaver} left the queue.")

    print_queue(queue)
    print()

    queue = clear_queue(queue)

    print_queue(queue)
    print()

    try:
        leaver, queue = leave_queue(queue)
    except IndexError:
        print("Cannot leave an empty queue.")
