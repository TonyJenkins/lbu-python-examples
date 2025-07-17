# Writing DRY Code

All the examples so far have been quite short. As programs get longer, we need a way
to split the code down into smaller units. These are _functions_. Functions allow the
programmer to keep things simple, and to create _building blocks_ that are useful in
many situations.

In the below examples, the first make use of functions from Python's _Standard Library_. Then
there are some where the programmer creates a function. See a later collecton of progrms for  examples that use functions from the Python Package Index.

_Terminology: A function is a useful chunk of code. Usually, it is passed some values,
and it returns some values (like calculating a square root). Related functions are
grouped into modules._

## Contents

Using _Standard Library_ functions:

- `circle_facts.py` - Display area and circumference of a circle, given the radius.
- `coin_toss.py` - Simulate a single coin toss.
- `coin_tosses.py` - Simulate a given number of coin tosses, and report results.
- `hello_name.py` - As usual, but this time fixing the capitalisation of the name entered.
- `many_sided_die.py` - Roll a die, given the number of sides.
- `string_obfuscate.py` - Disguise a message by adding random characters between letters.

Creating bespoke functions (some of which also use _Standard Library_ functions):

- `banner_print.py` - Print any string, with matching underline and (optionally) side bars and overline.
- `file_checker.py` - Determine whether a file exists in the current folder.
- `reverse_string.py` - Function to reverse a string, using a nifty trick.
- `super_die.py` - Function to roll an any-sided die, with a default of 6.
- `super_dice.py` - Function to roll any number of any-sided dice.
