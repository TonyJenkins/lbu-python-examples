# The Amazing Link Checker

A program that takes a list of web addresses from a file (provided
as a command line argument) and displays which are valid URLs.

Here "valid" is defined as returning an HTTP 200 (OK) result. Any other
code returned is displayed (probably 404, but others are possible). Or
if the domain lookup fails, that is printed instead.
