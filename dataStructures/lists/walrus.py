#!/usr/bin/python3

# the walrus operator reads chunks of data from a file like object
# returned by fp.
# in each iteration, the value of 'chunk' is printed to the console
# this allows you to read a large file in small chunks rather than reading
# the entire file into memory at once
while chunk := fp.read(200):
    print(chunk)
