class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    def __repr__(self):
        return "Robot(\"" + self.name + "\", " + str(self.build_year) + ")"
    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new = eval(x_repr)
    print(x_repr)
    print(new)
    print("Type of new:", type(new))
"""
The eval() function in Python is a built-in function that parses the expression
passed to it and runs Python code within the program.
It can be used to evaluate a wide range of expressions, including mathematical
expressions, variable assignments and function calls.
However, it's important to be 
"""
