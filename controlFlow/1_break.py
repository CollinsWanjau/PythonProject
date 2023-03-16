#!/usr/bin/python3

# break statements, breaks out of innermost enclosing 'for' or
# 'while' loops

# loops statemtents may have an else clause; it is executed when the
# loop terminates through exhaustion of the iterable 'with for' or when the condition
# becomes false, but not when the loop is terminated by a break statement

# this loop searches for prime numbers

# when used with a loop, the 'else' clause has more in common with the
# else clause of a try statement that it does with that of if types

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break;
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
