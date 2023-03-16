# Clean Up Actions

* The following points discuss more complex cases when an exception occurs:

* If an exception occurs during an execution of the try clause, the exception
may be handled by an `except` clause.If the exception is not handled by an 
except clause, the exception is re-raised after the finally clause  has
been executed

* The exception is re-raised after the finally clause has been executed

* If the finally clause executes a break, continue or return statement,
exceptions are not re-raised.
