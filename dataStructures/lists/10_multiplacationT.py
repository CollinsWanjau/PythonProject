#!/usr/bin/python3

import random
import math

# Create the multidimensional list
listNumber = [[0] * 10 for i in range(10)]

# Increment with outer for
for i in range(1, 10):
    # Increment with outer for
    for j in range(1, 10):
        # Assign the value to the cell
        listNumber[i][j] = i * j


# output the data
for i in range(1, 10):
    for j in range(1, 10):
        print(listNumber[i][j], end = ",")

    print()
