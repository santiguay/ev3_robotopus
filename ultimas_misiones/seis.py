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


#Mision 3: Almacenamiento de energia(30 puntos)
robot.drive_time(300, 0, 1000)
robot.turn(60)
robot.drive_time(200, 0, 2000)
robot.turn(-85)
mid_left_motor.run_time(100, 1100)
sleep(0.5)
mid_left_motor.run_time(-100, 1100)



#Mision 4: Granja Solar(20 puntos)
robot.turn(80)
robot.drive_time(200, 0, 1000)
robot.turn(70)
robot.drive_time(200, 0, 800)

#Mision 5: Red inteligente(manito)(20 o el mejor caso 30 puntos)
robot.turn(80)
mid_right_motor.run_time(-200, 600)
robot.turn(-90)
mid_right_motor.run_time(200, 600)

#Mision 13: Power-to-x(15)
robot.drive_time(-1,0,50)
robot.turn(120)
robot.drive_time(200, 0, 1500)
robot.turn(20)

#Sexta y ultima Salida
#Total de puntos logrados: 85 puntos
#Total de puntos acumulador: 295 puntos 


