#!/usr/bin/python3

# if the expression is a tuple it must be parenthesized

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x>=0])
