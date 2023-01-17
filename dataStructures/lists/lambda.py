#!/usr/bin/python3

# General syntax of lambda function
# lambda argument_list: expression
# the argument list consists of a comma separated list of args and
# the expression using these args
# you can assign the function to a variable to give it a name
sum = lambda x, y: x + y
print(sum(3, 4))
print('-------------------\n')

# convectional function definition
def sum(x, y):
    return x+y
print(sum(3, 4))
