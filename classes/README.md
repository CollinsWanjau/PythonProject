# Object Oriented Programming

* Classes and objects are the two main ascpects of OOP.

* A `class` creates a new `type` where objects are `instances` of the class.

* Objects can store data using ordinary variables that belong to the object.

* Variables that belong to an object or class are referred to as `fields`.

* Objects can also have functionality by using functions that belong to a class.

* Such functions are called `methods` of the class.

* Collectively, the fields and methods can be referred to as the `attributes`
of that class.

* Fields are of two types- they can belong to instance/object of the class or they
can belong to the class itself.They are called `instance variables` and `class variables`


## The `self`

* Class methods have only one specific diff from ordinary functions - they must
have an extra first name that has to be added to the beginning of the param
list.

* This particular variable refers to the object itself, and by convention, it is
given the name `self`.

## Classes

## Methods

###  The __init__ method

* The `__init__` method is run as soon as an object of a class is instantiated(i.e. created)

* The method is useful to do any initialization (i.e. passing initial values to your object)
you want to do with your object.

## Class And Object Variables

* The data part, i.e fields, are nothing but ordinary variables that are 
bound to the namespaces of the classes and objects.

* This means that these names are valid within the context of these classes and
objects only.That's why they are called `namespaces`.

* `Class Varibales` - they can be accessed by all instances of that class.

* `Object variables` - are owned by each individual object/instance of the class.
They are not shared and are not related in any way to the field by same name
in different instances

* Four major principles of OOP:
1. Encapsulation
2. Data Abstraction
3. Polymorphism
4. Inheritance

## A Minimal Class in Python

* A class object is created, when the definition is left normally, i.e. via
the end.This is basically a wrapper around the contents of the namespace
created by the class definition.

## Attributes

* Attributes are created inside a class definition.

* We can dynamically create arbitrary new attributes for existing instnaces
of a class

## Data Abastraction, Data Encapsualtion, and Information Hiding

### Definition of Terms

* `Encapsulation is seen as bundling of data with the methods that operate on data
that data.Information is wher some internal informartion is hidden`, so that
it can't be accidentally changed.

* `Data Abstraction` is present if both data hiding and data encapsulation
is present

* `Encapsulation`  is often accomplished by providing two kinds of methods
for attributes:
    1. The methods for retrieving or accessing the values of attributes are
        called `getter methods`.
    * `Getter methods` do not change values of attributes, they just return
        the values.
    2. The methods used for changing the values of attributes are called
        `setter` methods.

## Public, -Protected-, and Private Attributes

* `Public (name)` - these attributes can be freely used inside or outside a class
definition.

* `-Protected- (_name)` - Protected attributes cannot be used outside of class definition
unless inside a subclass definition.

* `Private (__name)` - This kind of attribute is inaccessible & invisible.
It's neither possible to read nor write to those attributes, except inside
the class definition. 

```
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
```
