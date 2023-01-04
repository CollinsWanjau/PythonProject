# a list of methods on list

list.append(x):
    add an item to the end of the list.Equivalent to 
    a[len(a):] = [X]

list.extend(iterable):
    Extend the list by appending all items from the iterable.Equivalent to
    a[len(a):] = iterable

list.insert(i, x):
    Insert at a given position.
    The first arg is the index of the element before which to insert, so
    "a.insert(0, x)" inserts at the front of the list, and "a.insert(len(a), x)"
    is equivalent to "a.append(x)"

list.remove(x):
    Remove the first item from the list whose value is equivalent to x.
    Raises ValueError if no such item is found

list.pop([i]):
    Remove at a given position in the list & return it.
    If no index is found, a.pop[] removes and returns the last item in the list

list.clear():
    Remove all items from the list. Equivalent to del a[:]

list.index(x[, start[, end]]):
    Return zero-based in the list of the first item whose value is equal to x
    Raises ValueError if there is no such value
    The optional args start and end are interpreted as in the slice notation and
    are used to limit to a particular subsequence of the list.
    The  returned index is computed relative to the beginning of the full sequence rather
    than the start of the arg

list.count(x):
    Return the number of times x appears on the list

list.sort(*, key = None, reverse = False):
    Sort of the items of the list in place
