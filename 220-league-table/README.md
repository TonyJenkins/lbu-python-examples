# Generating a League Table

Hopefully the concept of a _League Table_ for a sporting event is familiar! 

This table might appear on a web page, and would need to be updated after every
match played in the league. The program in this directory does that (actually
it recreates the table from scratch each time).

_Note: This program uses a Python class._

## How It Works

The program reads a file of results (see `results.txt`). This file contains
the result of every match in a format that has one line per match and looks 
like this:

```text
home_team,home_score,away_team,away_score
```

It is assumed that each line _is_ in this format.

This file is used to generate a list of the teams in the competition, and
objects are created for each. Then the file is re-read, and the objects
are updated. (This could all be done in one pass, but that code would be
scary!).

Finally the table is printed, using the `tabulate` module.

The number of points for a win or draw is configurable. The rules for
sorting the team is the common one (see code). Different rules could be
implemented by tweaking the `__lt__` method in the `Team` class.

There are two sample input files included here.

_Note: Code at the bottom of classes is for testing. It may or may not
work. There will be cruft._
