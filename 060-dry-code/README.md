# Writing DRY Code

All the examples so far have been quite short. As programs get longer, we need a way
to split the code down into smaller units. These are _functions_. Functions allow the
programmer to keep things simple, and to create _building blocks_ that are useful in
many situations.

In the below examples, the first make use of functions from Python's _Standard Library_. Then
there are some where the programmer creates a function in order to simplify the programming
task. 

Some programs further on in this collection are  examples that use functions from the 
Python Package Index. This require some installation of the packages.

_Terminology: A function is a useful chunk of code. Usually, it is passed some
(one or more) values, and it returns some (one or more) values (like calculating 
a square root, or giving the highest and lowest values in a sequence). The values passed in
are called _parameters_ or _arguments_. Related functions are grouped into modules. The
Standard Library is a collection of general-purpose modules._

## Contents

In many of these programs there is a small section of code as well as the function.
This is just there to test that the function works (which is obviously a _good thing_
to do).

It is also worth noting that if something goes wrong in a function, the best approach
is to `raise` an exception. This can then be handled by whatever is using the function
in whatever happens to be the best way.

Using _Standard Library_ functions:

- `circle_facts.py` - Display area and circumference of a circle, given the radius.
- `coin_toss.py` - Simulate a single coin toss.
- `coin_tosses.py` - Simulate a given number of coin tosses, and report results.
- `hello_name.py` - As usual, but this time fixing the capitalisation of the name entered.
- `many_sided_die.py` - Roll a die, given the number of sides.
- `string_obfuscate.py` - Disguise a message by adding random characters between letters.

Creating bespoke functions (some of which also use _Standard Library_ functions):

- `banner_print.py` - Print any string, with matching underline and (optionally) side bars and overline.
- `file_checker.py` - Determine whether a file exists in the current folder, using a command-line argument.
- `reverse_string.py` - Function to reverse a string, using a nifty trick.
- `super_die.py` - Function to roll an any-sided die, with a default of 6.
- `super_dice.py` - Function to roll any number of any-sided dice.
