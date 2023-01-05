#!/usr/bin/python3

# the initial expression in a list comprehension can be any arbitrary expression including
# another list comprehension

matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
]

# the following list comprehension will transpose rows and columns
print([[row[i] for row in matrix] for i in range(4)])
