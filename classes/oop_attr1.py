def hi(obj):
    print("Hi, i am " + obj.name + "!")
class Robot:
    say_hi = hi
x = Robot()
x.name = "Colloso"
print(Robot.say_hi(x))

"""
The proper way to do it:
    1. Instead of defining a function outside of a class definition and binding
    it to a class attr, we define a method directly inside
    2. A method is "just" a function which is defined inside a class
    3. The first parameter is used a reference to the calling instance
    4. This parameter is usually called self.
    5. Self corresponds to the Robot object x

We have seen that a method differs from a function only in two aspects:
    1. It belongs to a class, and it is defined within a class
    2. The first parameter in the definition of a method has to be a reference
    to the instance, which is called the method. This param is usually called
    `self`

For a class C, an instance x of C and a method m of C the following three methods 
