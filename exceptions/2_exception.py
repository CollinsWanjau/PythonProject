#!/usr/bin/python3
'''
the for loop iterates thru a list of the three exception classes, and for
each class, raises an exception of that class within a try_except block

the except block for class B is checked first.If the exception raised is an
instance of class B, the code inside the block will be executed and "B" will
be printed.Then the control goes out of the loop.If the exception raised os
not an instance of class B, the code will move to the next except block
'''
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D: 
        print("D")
    except C:
        print("C")
    except B:
        print("B")
