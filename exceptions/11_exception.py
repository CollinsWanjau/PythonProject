#!/usr/bin/python3
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
'''
exc allows disabling automatic exception chaining using the `from None` idiom

'''
