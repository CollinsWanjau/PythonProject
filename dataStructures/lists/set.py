#!/usr/bin/python3

# a set is an unordered collection with no duplicate elements
# basics uses include membership testing and duplicate entries

# set objects also support mathematical opertions like union, intersection
# difference  and symmetric difference
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # shows that duplicates have been removed

print('orange' in basket)   # fast membership testing

print('crabgrass' in basket)

# demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)    # unique letters in a
print(a -b) # letters in a but not in b
print(a | b)    # letters in a or b or both
print(a & b)    # letters in a and b
print(a ^ b)    # letters in a or b but not both

