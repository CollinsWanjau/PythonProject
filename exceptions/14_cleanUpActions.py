#!/usr/bin/python3

try:
    raise KeyboardInterrupt
finally:
    print("Goodbye, world")

'''
If a finally clause is present, the finally clause will execute as the last
task before the try statement completes

The finally clause runs whether or not the try statement produces an exception
'''
