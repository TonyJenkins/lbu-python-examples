# Useless Fact

This is a useless program, that prints a useless fact.

It does this through an API, and sending a request over the Internet (it's
an HTTP API). This uses the `requests` module (will need to be installed), the usual
way to work with APIs.

The response from the server comes back in JSON format, which has to be decoded.
There is another module for this, but happily `requests` bundles it, and provides
its own decoder.

_Note: This program may fall foul of firewalls, especially in Universities. That
may well be the explanation for unusual errors._
