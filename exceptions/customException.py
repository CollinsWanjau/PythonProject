#!/usr/bin/python3

# create a class that inherits from exception
class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):

        # Raise your own exception
        # You can raise the built in exceptions as well
        raise DogNameError
except DogNameError:
    print("Your dogs name can't contain a number")
