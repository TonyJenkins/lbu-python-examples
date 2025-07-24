# Word Dull

An implementation of a game where the user has a certain number of attempts
to guess a secret five-letter word.

The list of words is taken from a popular version of this game.

After each guess, correct letters are marked in green. Letters that are in the
answer, but not in the right place are in yellow.

Each letter is marked only once. This means that the marking is trivial for
words that have unique letters, but gets complex once you realise that words
can have duplicate letters!

_Note: The colouring should work on most terminals, but may not work inside a
terminal inside an IDE. See the docs for `colorama` on PyPi for more._
