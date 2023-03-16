#!/usr/bin/python3
num1 = "t"
num2 = 3
def divide(num1, num2):
    try:
        print(num1/num2)
    except(TypeError):
        print("both args must be numbers")
    except(ZeroDivisionError):
        print("num2 must not be zero")
