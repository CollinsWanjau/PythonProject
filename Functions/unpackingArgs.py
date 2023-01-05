#!/usr/bin/python3

# the reverse situation occurs when the args are already in list or tuple but need
# to be unpacked for a function requiring separate positional args

# for instance the range() expects the start and stop args
# if they are not available separately, write the function with the * operator to
# unpack the args out of a list or tuple
print(list(range(3, 6)))

args = [3, 6]
print(list(range(*args)))
