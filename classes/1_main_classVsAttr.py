#!/usr/bin/python3
from robot_asimov import Robot
for number, text in enumerate(Robot.Three_Laws):
    print(str(number+1) + ":\n" + text)
