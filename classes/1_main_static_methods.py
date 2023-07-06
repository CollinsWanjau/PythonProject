#!/usr/bin/python3
"""
Now it's possible to access the method via the class name, but we can't call
it via an instance
"""


from static_methods import Robot
Robot.RobotInstances()
x = Robot()
'''
This is treated as an instance method call and an instance method needs a ref
to the instance as the first param.

We want a method, which we can call via the instance name without the necessity
of passing a ref to an instance of it.The solution lies in static methods.
'''
x.RobotInstances()
