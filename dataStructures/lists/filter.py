#!/usr/bin/python3

'''filter(function, sequence)
Offers an elegant way to filter out all the elements of a sequence
"sequence", for which the function function returns true
Only if f returns True will the element be produced by the iterator
,which is the return value of filter(function, sequence)'''

"""In the following example we will filter out the first odd
    and then the even elements"""
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x : x%2, fibonacci))
print(odd_numbers)

print("-----------------\n")

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

print("-----------------\n")

even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
print(even_numbers)
