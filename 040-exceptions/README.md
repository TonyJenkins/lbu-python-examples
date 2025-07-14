# Exceptions

These programs illustrate EAFP-style error-handling.

EAFP ("Easier to Ask Forgiveness than Permission") means that the error is
allowed to happen, but is "caught". It is often neater, because error-handling
code can be kept away from the main "happy path" of the program.

## Contents

`grades.py` - Determine a student's grade based in their mark, which must be numeric and in range 0 to 100.
`sweets.py` - Divide a bag of sweets fairly between friends (trapping division by zero).
`temperature.py` - Temperature scale conversion, with check for valid (possible) temperature and numeric input.
`times.py` - Convert a number of minutes to hours and minutes, must be positive, and numeric.
`weight.py` - Convert kilograms to stone, must be non-zero, and numeric.

