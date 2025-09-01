#!/usr/bin/env python3


def generate_log_file_name_from_time():
    from datetime import datetime

    return f'{datetime.now().strftime("%Y%m%d-%H%M%S")}.log'


if __name__ == "__main__":
    pass
