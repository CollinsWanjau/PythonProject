#!/usr/bin/python3
try:
    myFile = open("mydata2.txt", encoding="utf-8")

# we can use `as` to access data and methods in
# exception class
except FileNotFoundError as exc:
    print("That file was not found")

    # Print out further data on the exception
    print(exc.args)
else:
    print("File :", myFile.read())
    myFile.close()
finally:
    print("Finished working with file")
