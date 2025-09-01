# Password Management

_Note: This folder contains a database-based solution to this problem._

The database used here is SQLite, a small database typically used
for managing small amounts of data like this. It would not be too
much work to convert to something like MariaDB - most of the work
would be in the SQL.

An interface to SQLite is part of the Python Standard Library, so nothing
needs to be installed. The `tabulate` module is used for output, so that
_does_ need to be available, or horrible things will happen.

The rest is, as near as make no difference, the same as the text-based
version. There is some additional dialogue, and usernames are validated,
but that's about it.

Oh, and some users can be admins. And because this is a database, the
users have unique numbers added. But that really is it.

There is an `allusers.py` script here, to provide a convenient way to see
the current state of play. (In the text-based solution we could just
look in the text file.)
