#!/usr/bin/python3
'''
raise_stmt ::=  "raise" [expression ["from" expression]]

* if no expressions are present, raise re-raises the exception that is
    currently being handled, which is also known as the active exception.
* If there isn't currently an active exception, a RuntimeError exception
    is raised indicating that this is an error

* Otherwise, raise evaluates the first expression as the exception object.
    It must be either a subclass or an instance of BaseException.
* If it is a class, the exception instance will be obtained when needed
    by instantiating the class with no arguments

* The type of the exception is the exception instance class, the value is
    the instance itself

* A traceback object is normally created automatically when an exception is
    raised and attached to it as the __traceback__ attribute, which is
    writeable
* You can create an exception and set your own traceback in one step using
    the with_traceback() exception method (which returns the same exception
    instance, with its traceback set to its argument), like so:

    raise Exception("foo occurred").with_traceback(tracebackobj)
'''

