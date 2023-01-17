#!/usr/bin/python3

'''the advantage of lambda operator can be seen when used in combination with
    map function which takes two arguments.'''
r = map(func, seq)
'''the first argument func is the name of the function and a second sequence(e.g. a list) seq
    .map() applies the function func to all elements of the sequences seq.
     Before Python3, map() used to return a list, where each element of the result list was
    the result of the function func applied on the corresponding element of the list or tuple
    "seq".
    With python3, it returns an iterator'''


