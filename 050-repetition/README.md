# Repetition

After _sequence_ and _selection_, here is _repetition_.

There are two types of repetition in programs. They could be both coded the same way, but usually
for convenience there are different ways available. Below are examples of both, viz:

- _determinate_ repetition, where it can be known before the loop starts how many executions there will be. These are
first below. (The number is known before the loop starts in the program, which is _not_ always known when the program is being written).
- _indeterminate_ repetition, where the number of executions cannot be known before the loop starts.

_Note: Some of these programs could be neater with the use of lists. See the next section along for examples
of that._

_Another Note: For clarity, some of the error-checking introduced in the previous two sections has been left out in
some of these examples._

## Contents

Using determinate (`for`) loops:

- `countdown.py` - Display an (exciting) space rocket countdown.
- `fizz_buzz.py` - (See https://en.wikipedia.org/wiki/Fizz_buzz) A counting game where numbers divisible by 3 are replaced
by `Fizz` and by 5 with `Buzz`. Displays the first 101 numbers.
- `grade_average.py` - Determine a student's average grade based on _five_ entered marks. (No error checking.)
- `grade_passes.py` - Count passed modules, where a student needs to pass 5 of 6, and display the result. (No error checking.)
- `password_check.py` - Check whether a password contains an uppercase letter, lowercase letter, special character, and digit.
- `table_of_times_tables.py` - Display the first 12 "times tables", as taught to school children.
- `times_table.py` - Display an arbitrary "times table". (No error checking.)

Using indeterminate (`while`) loops:

- `mark_average.py` - Determine a student's average grade based on an arbitrary number of marks. (Some error checking.)
- `password_changer.py` - The password complexity program above, but repeating until the password is OK.
- `password_checker.py` - Check two entered passwords match, exiting if they do, but with only three attempts.
