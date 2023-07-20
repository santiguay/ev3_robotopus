#!/usr/bin/env pybricks-micropython
"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
from time import sleep
import threading

from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
mid_right_motor = Motor(Port.B)
mid_left_motor = Motor(Port.C)


robot = DriveBase(left_motor, right_motor, wheel_diameter = 68.8, axle_track = 120)
# Creo las variables "speed" y "time"




#Creo la funcion en para ámbos procesos.
 #Lo ideal es usar el método ".join()", pero por cosas de la extensión no se ppueden utilizar, entonces se utiliza el módulo time con su función sleep.
    


#quinta mision
def quinta():
    robot.drive_time(300, 0, 1000)
    robot.turn(45)
    robot.drive_time(300, 0, 1100)
    robot.turn(-40)
    robot.drive_time(100, 0, 1500)
    robot.turn(-25)

    #vuelta al area home
    robot.drive_time(-300, 0, 600)
    robot.turn(55)
    robot.drive_time(-300, 0, 3000)
    
    

quinta()
