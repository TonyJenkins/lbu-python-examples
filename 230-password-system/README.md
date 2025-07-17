# Password System

There are two folders here, containing simple implementations
of the commands used to manage users on a Unix system.

First, is one that uses a plain text file (which is actually how
it works). The second uses an SQL database.

Passwords are encrypted, but just using a simple ROT-13. It would 
be easy to enhance the security (just need to edit one function,
which is the point!). Why not try?

The commands are (hopefully) self-explanatory. But note that a lot
of the common code is factored out into a module (keep it DRY).

