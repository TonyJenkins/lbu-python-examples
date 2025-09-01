# Dictionaries, Tuples, and Sets

Often the "trick" in writing an efficient program is picking the right
way to store the data. These programs illustrate how to use the remaining
three data structures provided in Python.

You _can_ do everything with lists, but sometimes great advantage can be 
gained from using something else.

## Contents

There are some examples using each of these structures here. Sometimes these
are just nifty ways to, for example, return multiple values from a function.
There is also at least one example of where the data structure might not be
the best. It's important to know what each can do!

### Dictionaries

A dictionary is a collection of key-value pairs. The intended use is that you lookup the
value associated with a key (like a book-based dictionary). Using a dictionary another way
(like finding the key associated with a given value) can lead to pain - after all, you wouldn't
read every definition in a dictionary looking for the right word!

First, some classic examples:

- `capitals.py` - A very simple quiz program.
- `class_list.py` - Read student names and grades, and print class list in grade order.
- `file_types.py` - List the files in the current folder and their assumed type (based on name).
- `nato.py` - Render a string in the NATO phonetic alphabet.
- `restaurant.py` - Sum up a food order using a lookup table.

Now, a common pattern is searching a collection of things, counting them to find something
like the most common. There is a special sort of dictionary for this. See these examples:

- `common_letter.py` - Find the most common letter in a string (probably useful in decryption).
- `duplicate_words.py` - Find all the words used more than once in a sentence.

### Tuples

Tuples are list-like, but the main difference is that the elements are not usually of the same type.
This means that they are handy for gathering together related values to pass in to, or out of,
a function.

- `format_records.py` - Neatly print a collection of scores for students, in descending order.
- `max_min.py` - A function that returns _both_ the highest and lowest values from a list.
- `reverse.py` - Return a string, along with the same string reversed.
- `top_student.py` - Find the name, username, and score of the best student on a test.

### Sets

The word _unique_ is a key indicator that sets will be useful. Another application is comparing
two collections, for example to find the common items. This can be done with a list (as usual) but
is easier with a set. (It is quite common to convert a list to a set, and back again).

- `common_letters.py` - Find the letters that are in both of two strings.
- `common_words.py` - As above, but words in a sentence.
- `random_list.py` - Generate a _list_ of a given length of unique random numbers.
- `unique_entries.py` - Prompt the user to enter a collection of words, and display the unique ones.
- `unique_scores.py` - Find the unique numbers in a _list_.
