#!/usr/bin/python3
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
'''
The `with` statement allows objects like files to be used in a way that ensures
they are always cleaned up promptly and correctly

After the statement is executed, the file f is always closed, even if a problem was
encountered while proccessing the lines
'''
