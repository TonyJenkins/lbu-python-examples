# Password Management

_Note: This folder contains a text-file-based solution to this problem._

## The Problem

For better or worse, most access to computer systems is still reliant 
on passwords. Various mechanisms exist to manage keeping records of 
users, their passwords, and the associated permissions. On traditional 
Unix systems the basic information (username, real name, password, etc) 
is stored in a plain text file usually  called `/etc/passwd`. 

Three command-line programs are used in the Unix world to maintain password information.

- `adduser` creates a new user, in the form of a new entry in the password file.
- `deluser` does the opposite, by removing the entry from the password file.
- `passwd` allows a user to change their password.

When a user attempts to access a system, the username and password 
they provide are checked against this file. This is done with a 
program called `login`.

This folder contains implementations of each of these programs.

### The File

The implementations that will work for a simplified password file. 
The format of the file is as follows. (In this example `password_string` 
marks where the encrypted passwords are (they would obviously be 
different on each line)).

```text
rms:Richard Stallman:password_string
ada:Ada Lovelace:password_string
jb:Justin Bieber:password_string
homer:Homer Simpson:password_string
```

The first field is the username, which always consists of lowercase 
letters. The second field is the user's real name, an arbitrary 
string. The third is their encrypted password. The three fields 
are separated with colons (``:``). There is no need for the 
username to be based on the real name in any way.

**This file is generated by the programs that maintain it (a default 
version is created when the system is installed), so it is safe to 
assume that it exists and is always formatted as expected, which is as shown. 
The order of the lines in the file is not significant.**

A sample file is included in this repo. In this example the 
passwords are "encrypted" with ROT-13. Which is better than 
nothing. Just about. There is also a program that will
generate sample `passwd` files.

The other programs are as follows:

<dl>
<dt>adduser</dt>
<dd>Adds a new entry to the file. It can be added anywhere, but here it is tacked on
the bottom as this is easiest. The user enters the desired username, the real name, 
and the password. The username is checked for uniqueness, but there is no need 
for the other fields.</dd>

<dt>deluser</dt>
<dd>Removes an entry from the file. This is based on the username, which 
is known to be unique. If the user is not found, the program should display a 
message to say nothing was changed.</dd>

<dt>passwd</dt>
<dd>Changes a user's password. The user enters their username, and their 
new password. As is customary, for verification, the user first enters 
their current password, and then the new password should be entered twice. 
No password should appear on the screen as it is typed. If the username is not found, the current password is invalid, or the passwords do not match, 
no change to the file should be made.</dd>

<dt>login</dt>
<dd>A simple "login" where the user enters a username and password, and 
the program reports whether or not they would be allowed to access the system. 
The password is not displayed as it is typed.</dd>
</dl>

## Other Notes

Many of the programs require the same functions, so these are factored out into a
module - DRY code is good!

Because the file location is hard-coded in that module, the functions _do not_ pass
the name of the file (or a file pointer) around. This design decision came as a result
of much thought and soul-searching. Password files do not move.

Depending on how you test the programs, you _may_ see passwords on the screen. This
is a terminal emulation issue. Using a standard Terminal or PowerShell should work,
but there might be issues with a terminal built in to an IDE.

