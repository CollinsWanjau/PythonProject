#!/usr/bin/python3
"""
A problem lurks in the definition of about.The only way to access the class info
__class_info is putting a class name in front of it.

No matter what we do, the solution will not be what we want.

We have no way of differentiating between the class Pet and its
"""


class Pet:
    _class_info = "pet animals"
    @staticmethod
    def about():
        print("This class is about " + Pet._class_info + "!")
class Dog(Pet):
    _class_info = "man's best friends"
class Cat(Pet):
    _class_info = "all kinds of cats"
Pet.about()
Dog.about()
Cat.about()
