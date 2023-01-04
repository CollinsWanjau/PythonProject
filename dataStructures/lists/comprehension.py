#!/usr/bin/python3

# lists provide a conscise way to create lists

# Common application are to make new lists where each element is the reault of 
# some operations applied to each member of another sequence or iterable, or to
# create a subsequence of those elements that ssatisfy a certain condition
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# now that this creates a variable named x that still exists after the loop completes
# we can calculate the list of squares without any side effects

squares = list(map(lambda x: x**2, range(10)))
print(squares)

# or

squares = [x**2 for x in range(10)]
print(squares)

# a list comprehension consists of brackets containing an expression followed by a for clause
# then zero or more for or if clauses.The result will be a new list resulting from evaluating
# the expression in the context of the for and if clauses which follow it

# the listcomp combines the elements of two lists if they are not equal

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# equivalent to

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
print(combs)
