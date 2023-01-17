#!/usr/bin/python3

C = [39.2, 36.5, 37.3, 38, 37.8]

# the map() function applies a lambda function to each element
# the lambda function is being applied to each element in the list
# 'c'.
# this lambda takes one input variable "x", and applies the operation
# on it

F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)
print("--------------------\n")
"""map() can be applied to more than one list.The lsits don't have
    to have the same length.
    Map() will apply its lambda function to the elements with 0th
    index, then to the elements with the 1st index until the n-th
    index is reached"""
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9] 

print(list(map(lambda x, y, z: x+y+z, a, b, c)))
print("----------------------\n")

print(list(map(lambda x, y: x+y, a, b)))
print("----------------------\n")

print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)))
print("----------------------\n")

"""If one list has fewer elements than the others, map will stop
    when the shortest list has been consumed"""
a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)))
