#!/usr/bin/python3

# when looping thru dictionaries, the key corresponding value can be retrieved
# at the same time using the items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
print('-------------------')

# when looping thru a sequence, the position index and corresponding value can be retrieved
# at the same time using the enumarate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
print('-------------------')

# to loop over two or more sequences at the same time, the entries can be paired with the
# zip function
questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("what is your {0}? It is {1}". format(q, a))
print('-------------------')

# to loop over a sequence in reverse, first specify the sequence in a forward direction and
# then call the reversed() function
for i in reversed(range(1, 10, 2)):
    print(i)
print('-------------------')
# to loop over a sequence in sorted order, use the sorted() function which return
# a new sorted list while leaving the source unaltered
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
print('-------------------')
# using set on a sequence eliminates duplicate elements
# the use of sorted in combination with set() over a sequence is an idiomatic way
# to loop over unique elements of the sequence in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)
print('-------------------')

# it is sometimes tempting to change to change a list while you are a looping over it, often
# it is simpler and safer to create a new list instead
import  math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

