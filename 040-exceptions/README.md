# Exceptions

These programs illustrate EAFP-style error-handling, which is usually handled
through _Exceptions_. These will have been obvious when previous programs
have failed and bleated about `ValueError`, `TypeError`, and the like.

This is `EAFP` error-handling.

EAFP ("Easier to Ask Forgiveness than Permission") means that the error is
allowed to happen, but is "caught". It is often neater, because error-handling
code can be kept away from the main "happy path" of the program.

Using this approach means that these programs can check the _type_ of input rather than
just the value. This is done by attempting to convert the `input` string into the required 
type, and catching the Exception if this fails.

## Contents

- `grades.py` - Determine a student's grade based on their mark, which must be numeric and in range 0 to 100.
- `pizza_price.py` - Now checking for integer input.
- `speed.py` - Checking for numeric input, allowing floating-point numbers.
- `sweets.py` - Divide a bag of sweets fairly between friends (trapping division by zero).
- `temperature.py` - Temperature scale conversion, with check for valid (possible) temperature and numeric input.
- `times.py` - Convert a number of minutes to hours and minutes, must be positive, and numeric.
- `weight.py` - Convert kilograms to stone, must be non-zero, and numeric.

