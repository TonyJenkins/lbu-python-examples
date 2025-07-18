# Introduction to Programming

## Assignment: Task 3

### The Problem

For better or worse, most access to computer systems is still reliant on passwords. Various mechanisms exist to manage keeping records of users, their passwords, and the associated permissions. On traditional Unix systems the basic information (username, real name, password, etc) is stored in a plain text file usually  called ``/etc/passwd``. Some other systems use a small database.

Various command-line programs are used in the Unix world to maintain password information.

* ``adduser`` creates a new user, in the form of a new entry in the password file.
* ``deluser`` does the opposite, by removing the entry from the password file.
* ``passwd`` allows a user to change their password.
* ``login`` determines whether or not a user is permitted to ask a system, by examining their username and password.

In addition, a utility to list all the current registered users of a system is often useful. That might be called ``allusers``.

This task involves developing implementations of each of these programs.

### The Task

Your task is to implement the four commands above, together with another utility that will list all the current users in some neat format. 

You will provide implementations that will work for a small embedded database. The database system to use is SQLite, an interface to which is provided as part of the Python Standard Library. Obviously your first task is to research into how SQLite databases can be accessed from Python.

A sample script is included in this folder of the repo. It creates the database table that you should use. Note that an SQLite database is a single file, and that this script will create it should it not exist.

Your programs should work as follows:

<dl>
<dt>adduser</dt>
<dd>Adds a new entry to the database. The user should enter the desired username, the real name, the password, and whether or not the user has admin rights. If the username already exists, an error should be shown and no entry should be made. It is fine for several users to have the same real name, the same password, and obviously several will have admin rights.</dd>

<dt>deluser</dt>
<dd>Removes an entry from the database. This should be based on the username, which is known to be unique. If the user is not found, the program should display a message to say nothing was changed.</dd>

<dt>passwd</dt>
<dd>Changes a user's password. The user should enter their username, and their new password. As is customary, for verification, the user should first enter their current password, and then the new password should be entered twice. No password should appear on the screen as it is typed. If the username is not found, the current password is invalid, or the passwords do not match, no change to the database should be made.</dd>
</dl>

The password itself should be stored in some encrypted form. Anything is fine, even a simple substitution or trivial obfuscation. There are no extra marks for doing something more complicated!

Your fourth program should be a simple "login" where the user enters a username and password, and the program reports whether or not they would be allowed to access the system. The password should not be displayed as it is typed, but you may want to print it out for testing purposes.

The final program should display a list of all current users. Any neat format is fine.

In all these programs it is fine to hard-code the name of the database. This will be needed by all of the programs, but you should still store it in only one place.

Likewise, it is quite possible that one or more of your programs could require the same functions. Such code should **not** be duplicated in multiple programs. (Most likely, a well designed solution will contain one module with many functions, and a set of quite short programs that use these.)

The database you will be working with is quite small, so there is no need to be too concerned about the efficiency of your solution. Certainly you should assume that the whole database can be held in memory without any performance hit (that is really the point of SQLite).

*In completing the tasks above you may use any module from the Python Standard Library that you find will help. You will have to use the SQLite library, but it will be very difficult to achieve good results without using others! You may use a package from PyPi to format the output of the command to list users if you want.*

*If you want to use serious encryption for passwords, you are welcome to use something like the ``cryptography`` module from PyPi, but there is no need to do so. Nor are there any extra marks for doing so. If you do use any modules from PyPi you should use a Virtual Environment (which should obviously not be in your repo), and include in your repo a clear statement of what you have used (the usual ``requirements.txt``) file is fine.*

### Examples

Since we are dealing with a database, it is difficult to provide examples that show all the possibilities. Here are some examples.

After creation, the database is empty:

```text
$ python3 allusers.py
No users in the database!
```

Adding a user makes an entry in the database:

```text
$ python3 adduser.py
Enter username: alan
Real Name: Alan Turing
Password: 
Admin? (y/n): y

$ python3 allusers.py
+-------+------------+-------------+------------+---------+
|   uid | Username   | Name        | Password   | Admin   |
+=======+============+=============+============+=========+
|     1 | alan       | Alan Turing | #####      | Yes     |
+-------+------------+-------------+------------+---------+
```

Note that the password is not displayed in the listing. It has been encrypted in the database. The user can now login with the correct password:

```text
$ python3 login.py
Enter username: alan
Password: 
Access Granted
```

Other users cannot, and nor can the single user if he gets the password wrong. (The specific errors are not great practice here, but are useful for debugging.) Note that passwords are not displayed.

```text
$ python3 login.py
Enter username: linus
Unknown User

$ python3 login.py
Enter username: alan
Password: 
Access Denied

```

A video showing other possibilities will be added to MyBeckett.
