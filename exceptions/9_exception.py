#!/usr/bin/python3
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
'''
if unhandled exception occurs inside an except section, it will have the exception
being handled attached to it and included in the error message
'''
