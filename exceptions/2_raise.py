#!/usr/bin/python3
try:
    print(1/0)
except:
    raise RuntimeError("Something bad happened")
'''
A similar mechanism works implicitly if a new exception is raised when an exception
is already being handled.
The previous exception is then attached as the new exception's __context__
attribute
'''
