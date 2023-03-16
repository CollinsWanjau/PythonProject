# ----------------GETTERS & SETTERS----------------
# Getters and setters are used to protect our objects
# from assigning bad fields or for providing improved
# output

class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is a getter
    @property
    def height(self):
        print("Retrieving the height")
        
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):

        # We protect the height from receiving a bad value
        if value.isdigit():

            # Put a __ before this private field
            self.__height = value
        else:
            print("Please enter only numbers for height")
    
    # This is the getter
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter only numbers for width")

    def getArea(self):
        return int(self.__height) * int(self.__width)

def main():
    aSquare = Square()

    height = input("Enter the height: ")
    width = input("Enter the width: ")

    aSquare.height = height
    aSquare.width = width

    print("Height :", aSquare.height)
    print("width :", aSquare.width)

    print("The Area is :", aSquare.getArea())



main()
