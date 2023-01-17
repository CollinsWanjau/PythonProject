#!/usr/bin/python3

# the condtions used in while and if statements can contain any operators, not
# just comparisons

# the comparison operators 'in' and "not in" are membership tests that dertemine
# whether a value is in (or not in) a container

# the operators "is" and "is not" compare whether two objects are really the
# same object

# all comparison operators have the same priority, which is lower than that of
# all numerical operators

# comparisons may be combined using boolean operators "and" and "or",and the outcome
# of a comparison (or any other Boolean expression) may be negated with "not"
# These have lower priorities than comparison operators; btw them, "not" has the
# highest priority and "or" the lowest
# A and not B or C # is equivalent to
# (A and (not B)) or C

# the boolean operators "and" and "or" are so called short-circuit operators; they
# are evaluated from lef to right, and evaluation stops as soon as the outcome is
# declared
# For example, if A and C are true but B is false, A and B and C does 
# not evaluate the expression C.
# When used as a general value and not as a Boolean, the return value of a 
# short-circuit operator is the last evaluated argument.

# it is possible to assign the result of a comparison or other Boolean expression to a variable
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
