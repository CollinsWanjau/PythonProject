#!/usr/bin/python3
"""
we will encounter problems, if we deifne the method about as a normal instance
method or a static mehtod

We also have to create instances of the Pet, Dog and Cat classes to be able to
ask what the class is about.

We have to write Pet.about(p)
"""


class Pet:
    _class_info = "pet animals"
    def about(self):
        print("This class is about " + self._class_info + "!")
class Dog(Pet):
    _class_info = "man's best friends"
class Cat(Pet):
    _class_info = "all kinds of cats"
p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()
