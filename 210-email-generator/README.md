# An Email Generator

Every year, new students arrive at Leeds Beckett, and need email
accounts. We assume these are not created manually, so this project
aims to simulate that process.

It also shows that we often need to develop programs that will generate
suitable test data. And that we need to deal with edge cases.

In this folder, find:

- `name_file_generator.py` - A (somewhat crufty, as usual) program to produce
a random sample input file.
- `generate_emails.py` - The program that does the generation.

The generator program uses the `names` module from PyPi, so that will need
to be available in order to run it. This is easier than coding something by
hand, and simpler than using more elaborate fake data generators.

There is also:

- `edge-cases.txt` - A few cases to test. These include names with spaces, hyphens,
and so on. These can be used as input separately.

_Interestingly, this program works in the (surprisingly frequent) case that a
student has only one name. The real one doesn't. Just saying._

## Full Details

_This was previously part of an assignment. Hence the style of the below spec._

### The Problem

The University of Poppleton enrols many new students at the start of each 
academic year. One part of this process involves creating email accounts 
for every new student. The format of these email addresses follows a particular
pattern, but creating them is a tedious process.

A program is required that will read a list of UCAS numbers (which will become 
student ID numbers) and corresponding student names and generate a corresponding 
list of student emails to be created. Both lists are stored in 
text files.

### The Task

The program should process a file containing a list of student IDs and names, and 
produce a second file containing the student IDs and the email address that 
should be created.

The names and IDs of new students are received in a file. It looks like this:

```text
c7090763 Velez, Hyun
c6542898 Salsbury, Debra Mary Adele
c9510348 Molina, Arianne Brittney
c5374186 Sampson, Lester
```

The first part is the student ID (at Poppleton that is always the same length). 
The rest of the line is the student's name, with family name separated from 
forenames by a comma. As shown, and as in real life, students have different 
numbers of forenames.

The first part of a student's email consists of their initials, separated by 
dots, their surname, and four random  digits (this last is to ensure that all 
students get unique emails). If a surname contains any non-alphabetic
character (as in "Fink-Nottle", "De Gea", or "O'Mahoney"), those characters are removed.

The second part is the University's domain, which is the same for all students. The 
result is rendered all in  lower case. So the above students would be given 
the following emails (once the domain has been added in):

```text 
c7090763 h.velez6435@poppleton.ac.uk
c6542898 d.m.a.salsbury5250@poppleton.ac.uk
c9510348 a.b.molina2382@poppleton.ac.uk
c5374186 l.sampson3346@poppleton.ac.uk
```

The program should take a file in the first format, and produce a file in the 
second. It is safe to assume that every line in the first file is formatted exactly as expected.

The program may ignore the (very remote) possibility of the program generating 
the same email for two different students.
