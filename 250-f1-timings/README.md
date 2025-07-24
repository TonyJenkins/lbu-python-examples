# Formula 1 Qualifying

This project processes a list of lap times (for example at a Formula 1 race),
and then ranks the drivers.

In the current version, the drivers are ranked by their fastest lap time. It
would be a small change to instead rank on average lap time. (It is done this
way because this is how _Qualifying_ for a race actually works.)

The driver details are read from `drivers.txt`. Details are correct as at
the Belgian Grand Prix 2025. Lap times are read from `lap_times.txt` or from
a command-line argument, if present. These are made up (see below).

There is also a crufty program to generate the lap times. To make the times 
vaguely realistic this includes some hacks to tweak the possible distribution
of times in favour of certain teams. This should mean that the more
successful drivers appear at the top, as in real life. (Without this hack every
driver would get roughly the same fastest time.)

The output is a formatted Leaderboard, in descending order of fastest time.
