#!/usr/bin/python3
'''
*The code raises an exception of the built-in 'exception' class, passing
    two arguments, 'spam' and 'eggs'.
* The exception is caught by the 'except' block, which creates a variable
    'inst' to hold the exception instance.
* 'type(inst)' is called and it will print the class of the exception, which
    is <class 'Exception'>.
* 'inst.args' is accessed which will print a tuple of the arguments passed
    to the exception, in this case '('spam', 'eggs')'
* After that, 'inst' is printed directly which will print the same as calling
    'str(inst)' which is a human-readable string representation of the
    exception, by default it is the class name followed by the arguments
    passed to the constructor
'''
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))   # the exception instance
    print(inst.args)    # arguments stored in .args
    print(inst)         # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
    x, y = inst.args    # unpack args
    print('x =', x)
    print('y =', y)
'''
Base classes

The following exceptions are used mostly as base classes for other exceptions

* exception BaseException - the base class for all built-in exceptions.It is
    not meant to be directly inherited by user-defined classes(for that use
    exception).If str() is called on an instance of this class, the rep of the
    arguments to the instance are returned, or the empty string when there are
    no arguments

    args - the tuple of arguments given to the exception constructor

* exception Exception - all built-in non-system-exiting are derived from this
    class.All user-defined exceptions should also be derived from this class

    * exception ArithmeticError - the base class for those built-in exceptions
    that are raised for various arithmetic errors: Overflow, ZeroDivisionError
    , FloatingPointError

* Exceptions which are not subclasses of Exception are not typically handled
    because they are used to indicate that the program should terminate
