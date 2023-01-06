#!/usr/bin/python3
import math
import random
numList = []

for i in range(5):
    numList.append(random.randrange(1, 9))

# create a value that will decrement for the outer loop
# its value is the index in the list
i = len(numList) - 1

while i > 1:
    j = 0

    print(f"\n {numList[j]} > {numList[j + 1]}")

    while j < i:
        if numList[j] > numList[j + 1]:

            print("Switch")

            temp = numList[j]

            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't switch")

        j += 1
        for k in numList:
            print(k, end = ", ")
        print()
    print("END OF ROUND")
    i -= 1

for k in numList:
    print(k, end = ", ")
print()
