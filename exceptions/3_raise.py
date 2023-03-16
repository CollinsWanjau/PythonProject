#!/usr/bin/python3
try:
    print(1/0)
except:
    raise RuntimeError("Something bad happened") from None
'''
Exception chaining can be explicitly suppressed by specifying None in the
`from` clause
'''
