#!/usr/bin/python3
"""
if we make the counter private, we need a possiblity to access and change
these private class attributes

We could use instance methods for this purpose
"""
class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstances(self):
        return Robot.__counter
if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    """
    This is not a good idea as number of robots has nothing to do with a single
    robot instance and secondly because we can't inquire the number of robots
    before we create an instance.

    If we try to invoke the method with the class name Robot.RobotInstances(),
    we get an error message, because it needs an instance as an argument
    """
    Robot.RobotInstances()
