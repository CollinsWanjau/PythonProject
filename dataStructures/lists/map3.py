#!/usr/bin/python3

# a function which applies a bunch of functions, which may be an
# iterable such as a list or a tuple
from math import sin, cos, tan, pi
def map_functions(x, functions):
    """map an iterable of functions on the object x"""
    res = []
    for func in functions:
        res.append(func(x))
    return res
family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

'''list comprehension
    def map_functions(x, functions):
        return [ func(x) for func in functions ]'''

