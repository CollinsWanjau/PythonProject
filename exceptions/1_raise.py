#!/usr/bin/python3

try:
    print(1/0)
except Exception as exc:
    raise RuntimeError("Something bad happened") from exc

'''
the 'from' clause is used for exception chaining.
* If given, the second expression must be another exception class or 
    inheritance
* If the second expresso is an exception instance, it will be attached to
    the raised exception as the __cause__ attribute(which is writeable)
* If the expresson is an exception class, the class will be instantiated
    and the resulting exception instance will be attached to the raised
    exception as the __cause__ attribute
