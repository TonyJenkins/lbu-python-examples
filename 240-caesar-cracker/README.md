# Caesar Cypher Cracker

A _Ceasar Cypher_ is a simple type of encryption where the alphabet is
simply shifted. It is easy to crack (there are only 25 possibilities), but
how to crack it automatically.

This was once set as an assignment, and many approaches were developed. Three
of the most popular are here. 

Obviously in "real life" a cracking program would probably work more by finding
the most likely decrypt, and then using human input. But here we try to complete
the whole process automatically.

## Spot the E (in `01_e_spotter`)

This simple approach finds the most common letter in the encrypted text, assumes
that corresponds to _e_, and thus calculates the rotation.

The plus side of this version is that it is easy to code, and will probably work.
The downside is that it would be defeated by, say, text about "Hannah from Alabama
who grows bananas and has an alpaca called Alan".

## Spot the Words (in `02_word_spotter`)

This is a variation on spotting the most common letter, that looks for the most
common words. The program tries each rotation in turn, and then looks for words
in the "decrypted" text. Once these words emerge, the text is _probably_ decrypted.

This is easy to code, but would be easy to defeat by padding any message with
repeated junk words.

## Spelling Sledgehammer (in `03_sledgehammer`)

This one _will_ work! This applies each rotation in turn, and spell-checks the result.
From this, the possible rotations can be ranked, and the one that contained the most
correctly spelled words is the right one.

While this version _will_ work (and will also spot if the file is not encrypted
as expected), you will probably see that it takes _a lot_ longer to run. There are
some obvious improvements, such as using a smaller dictionary, mind.

The present version also includes a hack to stop the checking if the percentage
of words observed is over (roughly) 90%. This is far too high - most likely 20%
would be enough.

## Notes

Each solution uses the same code for rotation. It's actually pulled from an
earlier example.

There are more ways to do this. For example, any single letter word found in the encrypted
text is very probably _a_. Looking for this, or words like _and_, or _the_ are all
good ways in.
