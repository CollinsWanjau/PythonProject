# DATA STRUCTURES

## Lists

The list data type has some more methods. Here are all of the methods of list objects:

**list.append(x)**
* Add an item to the end of the list. Equivalent to a[len(a):] = [x].

**list.extend(iterable)**
* Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

**list.insert(i, x)**
* Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

**list.remove(x)**
* Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

**list.pop([i])**
* Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

**list.clear()**
* Remove all items from the list. Equivalent to del a[:].

**list.index(x[, start[, end]])**
* Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

* The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

**list.count(x)**
* Return the number of times x appears in the list.

**list.sort(*, key=None, reverse=False)**
* Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

**list.reverse()**
* Reverse the elements of the list in place.

**list.copy()**
* Return a shallow copy of the list. Equivalent to a[:].

```
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting at position 4
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'
```

# NESTED LIST COMPREHENSIONS

* The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

* Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
```
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```
* The following list comprehension will transpose rows and columns:
```
[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
```
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

```
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

```
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```
# Del statement

* There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

```
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
[1, 66.25, 333, 333, 1234.5]
del a[2:4]
a
[1, 66.25, 1234.5]
del a[:]
a
[]
```
