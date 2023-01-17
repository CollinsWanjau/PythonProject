#!/usr/bin/python3

# function as objects
def mult_by_2(num):
    return num * 2

# a function can be assigned to another name
times_two = mult_by_2

print("4*2=", times_two(4))

# passed into other functions

def do_math(func, num):

    return func(num)

print("8 * 2 =", do_math(mult_by_2, 8))

# returned from a function

def get_mult_by_num(num):

    # create a dynamic function that will receive a value
    # and then return that value times the value passed
    # into the getFuncMultByNum()
    def mult_by(value):
        return value * num

    return mult_by

generated_func = get_mult_by_num(5)

print("5 * 10=", generated_func(10))

# Embedded in a dsa
listOfFuncs = [times_two, generated_func]

print("5 * 9 =",listOfFuncs[1](9))

# ------------------PROBLEM-------------------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd.
# The surrounding function will return a list of odd numbers

def is_it_odd(num):
    if num % 2 == 0:
        return False
    return True

def change_list(list, func):

    oddList = []

    for i in list:
        if func(i):
            oddList.append(i)

    return oddList

aList = range(1, 21)

print(change_list(aList, is_it_odd))

# --------------------FUNCTION ANNOTATIONS------------------
# It is possible to define the data types of attributes
# and the returned value with annotations, but they have no impact
# on how the function operates

def random_func(name: str, age: int, weight: float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))

# you don't get an error if you pass bad data
print(random_func(89, "Derek", "Turtle"))

# you can print the annotations
print(random_func.__annotations__)

# -------------------ANONYMOUS FUNCTIONS : LAMBDA -------------
# LAMBDA is like def, but rather then assign the function to a name
# it just returns it.Because there is no name that is why they are
# called anonymous functions.You can however assign a lambda function
# to a name

# format
# lambda arg1, arg2,.... : expression using the args

# Add values
sum = lambda x, y : x + y

print("Sum :", sum(4, 5))

# Use a ternary operator to see if someone can vote
can_vote = lambda age: True if age >= 18 else False

print("Can vote :", can_vote(16))

# Create a list of functions
powerList = [
        lambda x: x ** 2,
        lambda x: x ** 3,
        lambda x: x ** 4
        ]
for func in powerList:
    print(func(4))

# You can also store lambdas in dictionaries

attack = {
        'quick': (lambda: print('Quick Attack')),
        'power': (lambda: print('Power Attack')),
        'miss': (lambda: print('The Attack Missed'))
        }

attack['quick']()

import random

# keys() returns an iterable so we convert it into a list
# choice() picks a random value from that list
attackKey = random.choice(list(attack.keys()))

attack[attackKey]()

