#!/usr/bin/python3
numbers = [1, 4, 9, 16, 25]
print(numbers[0])
print(numbers[-1])
print(numbers[-3:])     # slicing returns a new list
print(numbers)

# all slice operations return a new list containing the requested elements.
# this means that the follwing
print(numbers[:])

# lists also support operations like concantenation
print(numbers + [36, 49, 64, 81, 100])

# unlike strings which are immutable, lists are a mutable type
cubes = [1, 8, 27, 65, 125]

cubes[3] = 64
print(cubes[3])

# you can also append
cubes.append(216) # add the cube of 6
cubes.append(7**3)  # add the cube of 7
print(cubes)

# assignments to properties is also possible
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list
letters[:] = []
print(letters)

# the builtin function len()
letters = ['a', 'b', 'c', 'd']
print(len(letters))

# it is possible to nest lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])

print(x[0][1])
