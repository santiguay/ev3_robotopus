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
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

#Inicializacion de objetos
ev3 = EV3Brick() 
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
sensor_giro = GyroSensor(Port.S2)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 68.8, axle_track = 123)

#Mision 8: Television (20 puntos)
ev3.speaker.beep()
robot.drive_time(180, 0, 2200)
robot.drive_time(-200, 0, 1450)

#Mision 7: Turbina eolica (30 puntos)
robot.turn(-55)
robot.drive_time(272, 0, 2100)
robot.turn(110)
for i in range(3):
    robot.drive_time(200, 0, 900)
    robot.drive_time(-150, 0, 600)
robot.drive_time(200, 0, 800)
robot.drive_time(-150, 0, 1600)

#Vuelta del robot al area home
robot.turn(140)
robot.drive_time(400, 0, 1800)

#Segunda Salida
#Total de puntos logrados: 50 puntos
#Total de puntos acumulador: 140 puntos 

