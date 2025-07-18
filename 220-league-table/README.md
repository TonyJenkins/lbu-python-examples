# Generating a League Table

Hopefully the concept of a _League Table_ for a sporting event is familiar! 

This table might appear on a web page, and needs to be updated after every
match played in the league. The program in this directory does that (actually
it recreates the table from scratch each time).

_Note: This program uses a Python class._

## How It Works

The program reads a file of results (see `results.txt`). This file contains
the result of every match in a format that has one line per match and runs:

```text
home_team,home_score,away_team,away_score
```

It is assumed that each line _is_ in this format.

This file is used to generate a list of the teams in the competition, and
objects are created for each. Then the file is re-read, and the objects
are updated. (This could all be done in one pass, but that code would be
scary!).

Finally the table is printed, using the `tabulate` module.
