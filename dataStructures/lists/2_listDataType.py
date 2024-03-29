#!/usr/bin/python3

# if the expression is a tuple it must be parenthesized

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x>=0])

# apply a function to all the elements
# abs() removes negative numbers
print([abs(x) for x in vec])

# call a method on each element

# The Python string strip() method is used to remove all the specified leading 
# and trailing characters from the beginning and the end of a string.
freshfruit = ['banana  ', ' loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2 tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized otherwise, there will be an error
print([(x, x**2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# list comprehensions can contain complex and nested functions
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
