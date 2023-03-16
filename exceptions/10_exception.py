#!/usr/bin/python3

# exc must be an exception instance or None
'''
`raise RuntimeError from exc`

This can be useful when you are transforming exceptions
'''
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
'''
The `as exc` is used to catch the exception and assign it to a variable
in this case, "exc" so that it can be inspected or handled in some way
'''
