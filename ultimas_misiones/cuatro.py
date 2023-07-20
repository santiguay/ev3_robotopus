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
from time import sleep
#Inicializacion de objetos
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 68.8, axle_track = 120)
med1_motor = Motor(Port.B)
med2_motor = Motor(Port.C)
sensor = GyroSensor(Port.S2)
def gyroMove(distance, speed):
    tg = sensor.angle()
    gain = 2
    robot.reset()
    
    while robot.distance() < distance: 
        correction = tg + sensor.angle() 
        turn_power = correction*gain
        robot.drive(speed, turn_power)



        



#Mision 14: Fabrica de juguetes(15 puntos)
ev3.speaker.beep()
robot.drive_time(220, 0, 950)
med1_motor.run_time(-25,3000)
med1_motor.run_time(100,1500)

#Mision 9: Dino(30 puntos)
robot.straight(-130)
robot.turn(-70)
sleep(0.5)

robot.drive_time(400, 0, 10000)

#Cuarta Salida
#Total de puntos logrados: 45 puntos
#Total de puntos acumulador: 205 puntos 