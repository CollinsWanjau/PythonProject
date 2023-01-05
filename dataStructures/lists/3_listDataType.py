#!/usr/bin/python3
import random
import math

randList = ["string", 1.234, 28]
print(randList[0])

onetoTen = list(range(10))

print(onetoTen)

randList = randList + onetoTen
print(randList)

print(len(randList))

first3 = randList[0:3]

for i in first3:
    print(f"{first3.index(i)} : {i}")

print(first3[0] * 3)

print("string" in randList)

print("Index of 'string': ", first3.index("string"))

print("How many strings :", first3.count("string"))

first3[0] = 'New string'

for i in first3:
    print(f"{first3.index(i)} : {i}")

first3.append("Another")

for i in first3:
    print(f"{first3.index(i)} : {i}")

