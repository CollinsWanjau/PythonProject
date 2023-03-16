#!/usr/bin/python3
'''
It is possible to write programs that handle selected exceptions.The
following asks the user for input until a valid integer has been selected
but allows the user to interrupt the program(using Control-C)
'''
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again")
    except (RuntimeError, TypeError, NameError):
        pass 

'''
* first the try clause(the statements between the try and except keywords)
  is executed
* if no exception occurs, the except clause is skipped and execution of the
  try statement is executed
* If an exception occurs during execution of the try clause, the reest of
  the clause is skipped.Then, if its type matches the exception named after
  the except keyword, the except clause is executed, and then execution
  continues after the try/except
* If an execution occurs which does not match the exception named in the 
  clause, it is passed on to outer try statements; if no handler is found,
  it is an unhandled exception.
'''
