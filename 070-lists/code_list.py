#!/usr/bin/env python3


def get_files_in_current_directory():
    from os import listdir
    from os.path import isfile

    return [f for f in listdir('.') if isfile(f)]


def filter_file_list_by_extension(files_to_filter, extension='.py'):
    return [f for f in files_to_filter if f.endswith(extension)]


if __name__ == '__main__':
    for file in sorted(filter_file_list_by_extension(get_files_in_current_directory())):
        print(f'- {file}')
