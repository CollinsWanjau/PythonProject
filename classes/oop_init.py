class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()

"""
we define the __init__ method as taking a parameter `name` (along with the
usual `self`), we also create a new field also called `name`.
* Notice there are two different variables even though they are both called
`name`.
* There is no problem because the dotted notation `self.name` means that there
is something called "name" that is part of the object called "self" and the
other `name` is a local variable.
* When creating new instance `p`, of the class `person`, we do so by using 
the class name, followed by the arguments in the parentheses: p = Person('Swaroop').

