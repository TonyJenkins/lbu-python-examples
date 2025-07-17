# Using Files

These programs take input from files, and write to files. There are many things
that go wrong when working this way; the most common is that the required files
does not exist and/or cannot be written.

For more file wrangling see also the `Unix Commands` collection.

## Contents

- `backup.py` - Create a copy of a file with `.bak` appended to the name.
- `caesar.py` - Apply a simple "Caesar Cypher" to a text file (shifting the alphabet). _Note that a negative "shift" should restore the file!_
- `check_file.py` - Check that a file exists in the current folder, and can be read.
- `de_punctuate.py` - Remove all the punctuation characters from a file, leaving just the
words (see also `word-count.py` below).
- `profanity.py` - Read a text file, and redact any unsuitable words (see `redact.txt`). 
- `rot-13.py` - Apply a simple encryption based on shifting the alphabet by 13 characters (so
applying it twice should restore the original file).
- `sort_file.py` - Sort the contents of a file, assuming one item per line. _(_Note: This
will be alphabetical order, so numbers will give strange results.)
- `sum_file.py` - Read a file of numbers, one per line (`numbers.txt`) and output the sum.
- `uniq.py` - Remove duplicate lines from a file.
- `word_count.py` - Count the words in a text file, and output the 10 most common.

_Note: Some of these programs are only slightly different! ROT-13 is jst a special case of a 
Caesar Cypher, for example._

## Test Utilities

In addition there is a (somewhat crufty) program to generate test data files, and some
plain text files for testing.

