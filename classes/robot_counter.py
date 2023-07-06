#!/usr/bin/python3
"""
Class methods are bound to a class.The first parameter of a class method is a ref
to a class i.e. a class object.

They can be called via an instance or the class name.
"""


class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
