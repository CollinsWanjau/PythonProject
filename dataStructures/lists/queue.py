#!/usr/bin/python3

# while appends and pops from the end of the list are fast, doing inserts from the beginning can be slow

# to implement a queue, use "collections.deque"

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

