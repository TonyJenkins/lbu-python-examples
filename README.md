# Example Python Programs

This repo contains various sample Python programs. See the notes below for more.

The programs are tested with [Python 3.13](https://www.python.org/downloads/), but should
work with any currently supported version of Python 3. The code tries to avoid "tricks" that
could obfuscate, but does aim to be _Pythonic_.

This code sort of accompanies [_Yet Another Python Book_](https://www.tony-jenkins.org.uk/pybook), the
source code for which is in [The Hungarian Phrasebook](https://github.com/TonyJenkins/hungarian_phrasebook).

_Most of this code was completed with the aid of GitHub Copilot, mostly when it wasn't being insanely
irritating by filling in totally inappropriate code!_

## Organisation

The programs are arranged in directories by topic. The numbers in the directory names
indicate (very roughly) the order in which they could be read. So "higher numbers"
may well use additional Python features. Some of these "higher numbers" also use
modules not included in the Standard Library (see notes below).

Directories with names starting with `0` contain simple programs showing basic programming
concepts. Directories starting `1` contain complete programs that use a range of
programming techniques. And those with names starting `2` contain more complex projects. There
is not much significance in the ordering of the directories starting `1` and `2`.

The should be a `README` file in each directory, which gives a brief idea of what each
program does.

## Requirements

The `requirements.txt` file includes all the external modules needed. It also includes
tools (see `black` below) used in the development. Alternatively, a good IDE will point
out which programs need external modules. All external modules are free, and from
[PyPi](https://pypi.org/).

## Code Formatting

The code is all formatted (quite ruthlessly) using `black` ([docs](https://black.readthedocs.io/)) with
its default settings. It should therefore comply with [PEP-8](https://peps.python.org/pep-0008/).
It is not impossible that certain IDEs will bleat about the formatting.

## Note on Development

These programs were developed on Linux using a heady mixture 
of [VS Code](https://code.visualstudio.com), [PyCharm](https://www.jetbrains.com/pycharm/),
and [neovim](https://neovim.io). They have not been tested on Windows 
or Mac. They should work on Mac. They should work on Windows, but if they don't, 
please consider your poor operating system choices.

A very few programs will work best if run from an external terminal rather than that 
embedded in an IDE. (It's all to do with _escape codes_.)

## Warranty (Ha!)

The programs are provided "as is" and without any warranty. They are not intended to be production
quality code, but rather to illustrate various Python features and techniques. Some of them may
well be borked, or may omit error handling for clarity. Caveat emptor!

See also the `LICENSE` in the repo.
