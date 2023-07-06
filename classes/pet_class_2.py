#!/usr/bin/python3
"""
A classmethod is the solution to all our problems.

We decorate about with a classmethod decorater instead of a
staticmethod decorator
"""

class Pet:
    _class_info = "pet animals"
    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")
class Dog(Pet):
    _class_info = "man's best friends"
class Cat(Pet):
    _class_info = "all kinds of cats"
Pet.about()
Dog.about()
Cat.about()
