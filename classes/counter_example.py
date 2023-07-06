#!/usr/bin/python3

"""
This example demonstrates how you can count instance with class attrs

Principally we would have written C.counter instead of type(self).counter,
because type(self) will be evaluated to "C" anyway.

type(self) makes sense, if we use such a class as a superclass
"""
class C:
    counter = 0
    def __init__(self):
        type(self).counter += 1
    def __del__(self):
        type(self).counter -= 1
if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
