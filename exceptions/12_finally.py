#!/usr/bin/python3
def bool_return():
    try:
        return True
    finally:
        return False
print(bool_return())
'''
If a finally clause includes a return statement, the returned value will
be the one from the finally clause's return statement, not the value form the
try clause's return statement
'''
