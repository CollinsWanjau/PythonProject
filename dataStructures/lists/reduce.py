#!/usr/bin/python3
import functools
print(functools.reduce(lambda x, y: x+y, [47, 11, 42, 13]))

print("----------------\n")

from functools import reduce
# defining the maximum of a list of numerical values using reduce
f = lambda a, b: a if (a > b) else b
print(reduce(f, [47, 11, 42, 102, 13]))

print("----------------\n")

# calculating the sum of the numbers from 1 to 100
print(reduce(lambda x, y: x + y, range(1, 101)))

print("----------------\n")

#calculating the product(the factorial)
print(reduce(lambda x, y: x*y, range(1,49)))
