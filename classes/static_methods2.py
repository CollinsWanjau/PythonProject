#!/usr/bin/python3
"""
Static methods don't need a reference to an instance.It's easy to turn a method
into a static method.

All we have to do is to add a line with "@staticmethod" directly in front of the
method header.
"""

class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    @staticmethod
    def RobotInstances():
        return Robot.__counter
if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(Robot.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
