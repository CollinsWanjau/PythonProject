#!/usr/bin/python3

# show how indexes work with a multiDimensional

listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = f"{i} : {j}"

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end = " || ")
    print()
