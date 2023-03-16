#!/usr/bin/python3

for line in open("myfile.txt"):
    print(line, end="")
'''
the problem with this code is that it leaves the file open for an
inderteminate amount of time after this part of the code has finished executing
'''
