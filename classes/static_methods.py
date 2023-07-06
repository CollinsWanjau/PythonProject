#!/usr/bin/python3
class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstances():
        return Robot.__counter
