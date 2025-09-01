# The Cat Shelter

_An example that, for some reason, spawned a life of its own._

_Before starting, Yes, it is a real cat. Yes, it has a shelter. Yes,
the shelter has a camera and security devices. Evidence is in the `img`
folder._

## The Problem

A kindly cat owner has installed a cat shelter in his garden. This acts 
as a refuge for his feline friend should the creature be caught outside in 
inclement weather at a time when its human servant is unavailable to open the 
back door.

The cat shelter contains a small camera, along with a motion detector and an 
RFID reader that detects a chip in a tag attached to the cat's collar. This 
is connected via WiFi to a laptop in the house, where a program creates a log of 
when the cat enters and leaves the shelter. If the chip is not detected, but 
motion is, it can be assumed that the neighbour's cat has trespassed into the 
shelter. In this case, a loud siren plays automatically, and jets of ice cold 
water are directed at the intruder. The ferocity of the attack is such that 
the cat can be assumed to have stayed for just one minute.

There has been a significant investment in this project, and the cat owner 
is keen to find out how much the shelter is being used. A program to analyse a 
daily log file is required.

## Detailed Specification

The laptop stores a data stream in a file that can be analysed. It records when a 
cat entered, when it left, and whether the cat was an intruder. One line is written 
for every cat activity, so a single line contains both the entry and departure times.

Times are stored as minutes, with a start of midnight. So midnight would be 
represented as zero, 1am is 60, and 9:30am would be 570 (9 x 60 + 30). There 
is one file created each day.

The cat shelter is small, so there can only be one cat in it at a time. It is 
often empty as the cat likes to bask on the roof.

The format of the file is shown by the following short sample.

```text
OURS,600,630
THEIRS,700,701
OURS,842,900
THEIRS,1000,1001
THEIRS,1010,1011
END
```

So we see that the correct cat (``OURS``) entered the shelter at 
10:00am (time 600), and stayed for 30 minutes (630 - 600). A 
different cat entered at time 700 which is 11:40, and swiftly left, having
been attacked with sound and water. And so on.

The data stream ends ``END``, which is written automatically 
before the file closes at 23:59. The shelter is never occupied at this time
(the cat being indoors in its basket). 

It is safe to assume that the file is always in this format.

The required output from the analysis program will be:

* The total number of times the correct cat has entered the house.
* The number of times intruding cats have been doused with water.
* The total time spent in the house by the correct cat.
* For the correct cat only, the average duration of each visit, the 
duration of the longest visit, and the duration of the shortest visit.

The name of the data file should be provided as a command-line 
argument. The program should therefore run from the command-line. It should 
handle the common errors associated with files on the command-line, such as
missing arguments, files that cannot be opened, and so on.

 ## Note

 This folder also includes a (somewhat crufty, as usual) program for generating
 test data files.
