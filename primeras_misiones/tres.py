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
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

#Inicializacion de objetos
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
med2_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 68.8, axle_track = 123)
sensor = GyroSensor(Port.S2)
def gyroMove(distance, speed):
    tg = sensor.angle()
    gain = 2
    robot.reset()
    
    while robot.distance() < distance: 
        correction = tg + sensor.angle() 
        turn_power = correction*gain
        robot.drive(speed, turn_power)
#Mision 6: Auto hibrido (20 punntos + pila recargable (dino) )
med2_motor.run_time(300, 700)
gyroMove(800, 200)
robot.turn(15)
med2_motor.run_time(-300, 600)
sleep(0.5)
med2_motor.run_time(300, 600)

#Regreso del robot al area home
robot.drive_time(-500,0, 3000)

#Tercera salida
#Total de puntos logrados: 20 puntos
#Total de puntos acumulados: 160 puntos
