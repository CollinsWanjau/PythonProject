l = [3, 8, 9]
s = repr(l)
print(s)
if l == eval(s):
    print("True")
else:
    print("False")
if l == eval(str(l)):
    print("True")
"""
__str__ is used if the output should be for the end user or if it should
be nicely printed.

__repr__ on the other hand is used for the internal representation of an
object.
"""
