#!/usr/bin/python3

# in stacks the last element added is the first item retrieved ("last in, first out").
# To add an item to the top of the stack, use append().
# to retrieve an item from the top of the list use pop() without an explicit index
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
