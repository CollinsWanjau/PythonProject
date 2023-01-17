#!/usr/bin/python3

'''

Order Number    Book Title and Author              Quantity     Price per Item
34587           Learning Python, Mark Lutz             4          40.95
98762           Programming Python, Mark Lutz          5          56.80
77226           Head First Python, Paul Barry          3          32.95
88112           Einführung in Python3, Bernd Klein     3          24.99

Write a Python program, which returns a list with 2-tuples. Each tuple consists
of a the order number and the product of the price per items and the quantity. 
The product should be increased by 10,- € if the value of the order is smaller 
than 100,00 €.
Write a Python program using lambda and map.

'''
min_order = 100
orders = [
        [34587, "Learning Python, Mark Lutz", 4, 40.95],
        [98762, "Programming Python, Mark Lutz", 5, 56.80],
        [77226, "Head First Python, Paul Barry", 3, 32.95],
        [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

invoice = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),\
        map(lambda x: (x[0], x[2]*x[3]), orders)))
print(invoice)

'''
The same bookshop, but this time we work on a different list.
The sublists of our lists look like this: [ordernumber, (article number, 
quantity, price per unit), ... (article number, quantity, price per unit) ] 
Write a program which returns a list of two tuples with 
(order number, total amount of order).
'''
from functools import reduce
orders = [
        [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],
        [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
        [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
        [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)]
        ]
min_order = 100
'''
the line of code is using the 'map()' function to apply the lambda
function to each elements on orders list
The lambda() takes one input variable 'x', which is an element of the
'orders' list.It extracts the first element of 'x', which is the order
number, and maps a nested lambda function to the remaining elements of 
'x' which are themselves lists.
The nested lambda() takes one input variable 'y' which is a sub-list of
the order, it extracts the second and the third element of the 'y' and
multiplies them
'''
invoice_totals = list(map(lambda x : [x[0]] +\
    list(map(lambda y : y[1]*y[2], x[1:])), orders))
print(invoice_totals)
print("------------------\n")
'''
this line of code is using the 'map()' function to apply the lambda()
to each element in the 'invoice_totals' list
The lambda() takes one input variable 'x', which is an element of the
'invoice_totals' lsit.It extracts the first element of 'x', which is
the order number, and applies the 'reduce'() to the remaining elements
of 'x' using the lambda function.
The reduce function applies the given lambda function cumulatively to
the elements of the input list, from left to right, so as to reduce it
to a single value
'''
invoice_totals = list(map(lambda x : [x[0]] +\
        [reduce(lambda a, b: a+b, x[1:])], invoice_totals))
print(invoice_totals)
print("------------------\n")

invoice_totals = list(map(lambda x : x if x[1] >= min_order else\
        (x[0], x[1] + 10), invoice_totals))
print(invoice_totals)
print("------------------\n")

