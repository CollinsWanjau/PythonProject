class Robot:
    pass
x = Robot()
y = Robot()
x.name = "Colloso"
x.build_year = "1979"
y.name = "Caliban" 
y.build_year = "1993"
print(x.name)
print(y.build_year)
print(x.__dict__)
print(y.__dict__)
print("-------------------")
Robot.brand = "Kuka"
print(x.brand)
x.brand = "Thales"
print(Robot.brand)
print(y.brand)
Robot.brand = "Thales"
print(x.brand)
print(x.__dict__)
print(y.__dict__)
print(Robot.__dict__)
# print(x.energy)

"""
We can dynamically create arbitrary new attributes for existing instances
of a class.
We do this by joining an arbitrary name to the instance name

To know whats happening internally: The instances possess dictionaries __dict__
,which they use to store their attributes and their corresponding values:
"""

"""
Binding attributes to objects is a general concept in Python.Even function
names can be attributed.You can bind an attribute to a function name in the
same way, we have done far to other instances of classes
"""
def f(x):
    return 42
f.x = 42
print(f.x)
