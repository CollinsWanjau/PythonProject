#!/usr/bin/python3
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

'''
* exception OSError - this exception is raised when a system function returns
    a system-related error, including I/O failures such as 'files not found'
* the final block is a catch-all block that will catch any other exceptions
    that are not caught by the previous two blocks
