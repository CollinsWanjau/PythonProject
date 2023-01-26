class Robot:
    """Represents a robot, with a name"""

    # A class variable, counting the number of robots
    population = 0


    def __init__(self, name):
        """Initializes the data"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1
    

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working,".format(
                Robot.population))
            
    def say_hi(self):
        """Greeting by the robot


        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))
print(Robot.__doc__)

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

"""
* `Population` belongs to the `robot` class and hence is a class variable.

* The `name` variable belongs to the object(it is assigned using `self`) and
hence an object variable.

* We refer to the `population` class variable as `Robot.population` and not
as `self.population`.

* We refer to the object variable `name` using `self.name`. notation in the
method of that object.

* Instead of `Robot.population`, we could have also used `self.__class__.population`
because every object refers to its class via the `self.__class__` attribute.

* The `how_many` is actually a method that refers to the class and not object.
We can refer to it as `classmethod` or a `staticmethod` depending on whether
we need to know which class we are part of.

* Since we refer to a class variable, let's use `classmethod`.

* We have marked the `how_many` method as a class method using a `decorator`.

* Decorators can be imagined to be a shortcut to calling a wrapper function
(i.e. a function that "wraps" around another function so that it can do something
before or after the inner function), so applying the `@classmethod` decorator
the same as calling:
    ```
    how_many = classmethod(how_many)

* All class members are public.One exception: If you use data members and name
them using double underscore prefix such as `__privatevar`, Python will use
name-mangling to effectiviely make it a private variable.

* The convention followed is that any variable that is used within the class/
object should be initialized with a double underscore prefix and all other names
are public and can be used by other classes/objects.
"""

