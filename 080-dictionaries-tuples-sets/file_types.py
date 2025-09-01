#!/usr/bin/env python3


def get_files_in_current_directory():
    from os import listdir
    from os.path import isfile

    return [f for f in listdir(".") if isfile(f)]


def guess_file_type_from_extension(file_name):
    from os.path import splitext

    known_types = {
        "c": "C Program",
        "cpp": "C++ Program",
        "json": "JSON Data",
        "md": "Markdown Document",
        "mmd": "Mermaid Diagram",
        "py": "Python Program",
        "pyc": "Python Byte Code",
    }

    _, extension = splitext(file_name)

    return known_types[extension[1:]]


if __name__ == "__main__":
    for file in sorted(get_files_in_current_directory()):
        try:
            print(f"- {file}: {guess_file_type_from_extension(file)}")
        except KeyError:
            print(f"- {file}: Unknown")
