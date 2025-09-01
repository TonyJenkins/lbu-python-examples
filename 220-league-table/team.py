#!/usr/bin/env python3


class Team:

    from conf import WIN_POINTS as POINTS_FOR_A_WIN
    from conf import DRAW_POINTS as POINTS_FOR_A_DRAW

    def __init__(self, name):
        self.name = name
        self.won = self.drawn = self.lost = 0
        self.scored = self.conceded = 0

    @property
    def played(self):
        return self.won + self.drawn + self.lost

    @property
    def difference(self):
        return self.scored - self.conceded

    @property
    def points(self):
        return self.won * Team.POINTS_FOR_A_WIN + self.drawn * Team.POINTS_FOR_A_DRAW

    def play_match(self, points_for, points_against):
        self.scored += points_for
        self.conceded += points_against

        if points_for > points_against:
            self.won += 1
        elif points_for < points_against:
            self.lost += 1
        else:
            self.drawn += 1

    def league_numbers(self):
        return (
            self.name,
            self.played,
            self.won,
            self.drawn,
            self.lost,
            self.scored,
            self.conceded,
            self.difference,
            self.points,
        )

    def __lt__(self, other):
        if self.points != other.points:
            return self.points > other.points
        elif self.difference != other.difference:
            return self.difference > other.difference
        elif self.scored != other.scored:
            return self.scored > other.scored
        else:
            return self.name < other.name


if __name__ == "__main__":
    t = Team("Poppleton")
    for home, away in ((20, 0), (12, 12), (12, 24)):
        t.play_match(home, away)
        print(t.league_numbers())

    t2 = Team("York")
    for home, away in ((20, 20), (18, 12), (32, 24)):
        t2.play_match(home, away)
        print(t2.league_numbers())

    print()
    print(t.league_numbers())
    print(t2.league_numbers())
