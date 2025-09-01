#!/usr/bin/env python3


def banner_print(text, character="*", overline=True, sidebars=True):
    length = len(text) + 4

    if overline:
        print(character * length)

    if sidebars:
        print(f"{character} {text} {character}")
    else:
        print(f"  {text}  ")

    print(character * length)


if __name__ == "__main__":
    banner_print("Hello, World!")
    print()
    banner_print("Hello, World!", character="-")
    print()
    banner_print("Hello, World!", character="-", overline=True, sidebars=False)
    print()
    banner_print("Hello, World!", character="-", overline=False)
    print()
    banner_print("Hello, World!", character="-", overline=False, sidebars=False)
