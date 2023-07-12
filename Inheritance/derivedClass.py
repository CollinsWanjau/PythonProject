#!/usr/bin/python3

class BaseClass:
    def my_method(self):
        print("BaseClass method")

class DerivedClass(BaseClass):
    def my_method(self):
        print("DerivedClass method")

obj = DerivedClass()
obj.my_method()
