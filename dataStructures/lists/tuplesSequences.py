#!/usr/bin/python3

# tuples and sequences

# a tuple consists of a number of values separated by commas
t = (12345, 54321, 'hello!')

print(t[0])

# tuples may be nested

u  = t, (1,2,3,4,5)
print(u)

# tuples are immutable
# t[0] = 8888
# print(t)

# though tuples may be similar to lists, they are often used in different situations
# tuples are immutable, and usually contain a heterogenous sequence of elements that
# are accessed via unpacking or indexing
# lists are muatable, and their elements are usually homogenous
# but they can contain mutable objects
v = ([1,2,3], [3,2,1])
print(v)

# a special problem is the construction of tuples containing 0 or 1 items
# empty tuples are constructed by an empty pair of parenthesis
# a tuple is constructed by following a value in comma
empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing: 
# the values 12345, 54321 and 'hello!' are packed together in a tuple. 
x, y, z = t

# this is sequence unpacking and works for any sequence on the right hand side
# Sequence unpacking requires that there are as many variables on the left side 
# of the equals sign as there are elements in the sequence. 
