# Maths Test

A maths test where the program ganerates 10 simple arithmetic questions, and prompts the
user to enter the answer.

Addition, subtraction, and multiplication are random. Division is "fixed" so that the answer
is an integer (this avoids precision issues). Subtraction _can be_ fixed so that the answer
is a positive value.

At the end the user is given a rating based on their performance.

Various config lurks in `conf.py`. This can be used to control what types of problems are
generated, whether to fix subtraction, maximum values, etc.
