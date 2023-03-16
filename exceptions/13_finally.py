#!/usr/bin/python3
def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
print(divide(2, 1))
print(divide(2, 0))
print(divide("2", "1"))

'''
The finally clause is executed in any event.

The typeError raised by dividing two strings is not handled by the except
clause and therefore raised after the finally clause has been executed
'''
