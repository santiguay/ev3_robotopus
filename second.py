#!/usr/bin/env pybricks-micropython
"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

#Librerias para importar que importan cosas importantes.
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

#Inicializacion de objetos
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 68.8, axle_track = 120)
med1_motor = Motor(Port.B)
med2_motor = Motor(Port.C)

#Tercera mision
ev3.speaker.beep()
robot.drive_time(280, 0, 800)
med1_motor.run_time(-25,3000)
med1_motor.run_time(100,1500)
robot.straight(-150)
med2_motor.run_time(125,600)
robot.turn(17)
robot.drive_time(300,0, 1500)
