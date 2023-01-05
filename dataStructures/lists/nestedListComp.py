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

# as we saw before, the innermost comprehension is evaluated in the context of the for that
# follows it
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# which in turn is the same as
transposed = []
for i in range(4):
    # the following lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# in the real world you should use the built-in function zip()
print(list(zip(*matrix)))
