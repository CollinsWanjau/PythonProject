#!/usr/bin/python3

import random
import math

numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))

print(numList.sort())
print(numList.reverse())
print(numList.insert(5, 10))
for k in numList:
    print(k, end = ", ")
print()
