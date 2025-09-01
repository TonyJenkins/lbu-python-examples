#!/usr/bin/env python3

import sys
import tabulate

from team import Team


def split_result_line(line_from_results_file):
    home, home_score, away, away_score = line_from_results_file.split(",")

    return home, int(home_score), away, int(away_score)


def get_team_names(results_file):
    teams_list = set()

    with open(results_file, "r") as rf:
        for result in rf.readlines():
            home, _, away, __ = split_result_line(result)

            teams_list.add(home)
            teams_list.add(away)

    return list(teams_list)


def create_league(team_name_list):
    blank_table = []

    for name in team_name_list:
        blank_table.append(Team(name))

    return blank_table


def update_table(current_table, team_name, scored, conceded):
    for team in current_table:
        if team.name == team_name:
            team.play_match(scored, conceded)
            return current_table

    return current_table


def play_matches(results_file, table):
    with open(results_file, "r") as rf:
        for result in rf.readlines():
            home, home_score, away, away_score = split_result_line(result)

            table = update_table(table, home, home_score, away_score)
            table = update_table(table, away, away_score, home_score)

    return table


def print_the_table(team_list):
    team_list.sort()

    table_data = [
        ["Team", "P", "W", "D", "L", "F", "A", "Diff", "Pts"],
    ]

    for team in team_list:
        table_data.append(team.league_numbers())

    print(tabulate.tabulate(table_data, headers="firstrow", tablefmt="grid"))


def make_the_league_table(results_file):
    teams = get_team_names(results_file)
    table = create_league(teams)
    table = play_matches(results_file, table)
    print_the_table(table)


if __name__ == "__main__":
    try:
        make_the_league_table(sys.argv[1])
    except (IndexError, FileNotFoundError,):
        print(f"Usage: python3 {sys.argv[0]} <results_file>")

