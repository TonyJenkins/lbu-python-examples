# Unix Commands

This directory contains implementations of various Unix file commands.

These can be implemented using the `shutil` or `os` modules from the Standard
Library, but that is no fun. The versions here are written with
the standard Python file operations where possible.

## Contents

- `cat.py` - Display a file on the screen.
- `cp.py` - Copy a file to another.
- `mv.py` - Rename (move) a file.
- `rm.py` - Delete (remove) a file.

- `diff.py` - Determine whether or not two files are the same (i.e. have the same content).
- `nl.py` - Display a file with line numbers.
- `wc.py` - Count lines, words, and characters in a file.

- `grep.py` - Find lines in a file that contain a given pattern.
- `spell.py` - A very basic spell checker.

_Note: The spell checker uses its own dictionary, located in the same folder. It would be
better to use the system dictionary if that existed, which it would on Linux or Mac,
but probably not on Windows. This could probably be coded better, to be honest._
