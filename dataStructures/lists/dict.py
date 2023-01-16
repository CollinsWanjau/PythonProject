#!/usr/bin/python3

# dictionaries are indexed by a range of numbers, dictionaries are indexed by
# keys, which can ba any immutable type; strings and numbers can always be keys

# tuples can be used as keys if they only contain strings, numbers or tuples
# if a tuple contains any mutable object either directly or indirectly it cannot
# be used as a key
#
# You can't use lists as keys since lists can be modified in place using index
# assignments, slice assignments, or methods like append and extend
#
# Performing list(d) on a dictionary returns a list of all  keys used in the dict
# In insertion order, if u want it sorted just use sorted(d)

# To check if a single key is in a dictionary use 'in'
tel = {'jack':4098, 'sape':4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

# the dict builds dictionaries directly from sequence of key value pairs
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# dict comprehensions can be used to create dictionaries from arbitrary key and value
# expressions
print({x: x**2 for x in (2,4,6)})

# when keys are simple strings then you can specify pairs using keyword args
print(dict(sape = 4139, guido = 4127, jack = 4098))
