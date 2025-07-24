# Park Run Times

This program processes a stream of data (entered at the keyboard), and 
generates some statistics.

There are a bunch of ways to do this. The approach here is enough to get
the basic job done. 

## The Problem

Poppleton Park Run is a monthly family fun run around Poppleton Park. Family groups run, jog, walk, or crawl
around their local park in a generally friendy way. The organisers publish the times of runners
at various points along the course around the park's perimeter. These times are eventually processed and published
on a website.

Automatic timing apparatus positioned around the park uses advanced computer vision techniques to read the numbers 
on each runner's singlet as they pass, and record this along with the elapsed time. These times need to be 
processed so that they can be posted on the website.

## The Task

A program is required that will process the data stream from one of the timing devices to produce 
some useful statistics. The chosen device is half way round the course, and is is known that every runner will
pass it at most once.

The data stream from the timing apparatus consists of the runner's number (as read from their singlet), and a time
in seconds, which is the time since the runner left the start. This is used because runners tend 
to start at different actual times. (It also means that the time can go down as well as up in the stream (think
about it)).

The two elements on the line are separated by two colons (`::`), and each data item 
appears on its own line. So, for example, here:

```text
0012::239
01921::256
```

runner with number `0012` passed 239 seconds after starting, and runner `01921` is slightly slower, passing at
256 seconds.

The data stream ends when the operator powers off the apparatus. Just before shutting down it sends the single 
line `END` to mark the end of the stream.

The required output is:
* The total number of runners who have been seen.
* The average time recorded, rendered in minutes and seconds.
* The fastest time recorded at this point, rendered in minutes and seconds.
* The slowest time recorded at this point, rendered in minutes and seconds.
* The number of the runner recording the fastest time (or the first one to do so, if there are several).

The apparatus is fallible, especially if a runner's singlet is dirty, so there may
be errors in the data.
