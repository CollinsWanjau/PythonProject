#!/usr/bin/python
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close
'''
the use of the else clause is better than adding additional code to the
try clause because it avoids accidentally catching an exception that 
wasn't raised by the code being protected by the try...except
'''
