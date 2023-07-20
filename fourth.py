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
speed = -100
time = 1000
#Se definen las funciones para el mobimiento por separado del motor
def move_motor1(speed, time):
    mid_right_motor.run_time(-speed,time)

def move_motor2(speed, time):
    mid_left_motor.run_time(speed, time)


#Define the threads. Para poderhacer multitareas, necesito usar los hilos del procesador para poder unirlos mediante mis insancias del módulo thread.
t1 = threading.Thread(target=move_motor1, args= (speed, time))
t2 = threading.Thread(target=move_motor2, args= (speed, time))

#Creo la funcion en para ámbos procesos.
def levante(time):
    t1.start()
    t2.start()
    sleep(time) #Lo ideal es usar el método ".join()", pero por cosas de la extensión no se ppueden utilizar, entonces se utiliza el módulo time con su función sleep.
    


#quinta mision
def quinta():
    robot.drive_time(300, 0, 1000)
    robot.turn(45)
    robot.drive_time(300, 0, 1600)
    robot.turn(-27)
    robot.drive_time(300, 0, 300)
    robot.drive_time(200, 0, 250)
    robot.turn(67)
    robot.drive_time(200, 0, 800)
    robot.turn(90)
    robot.drive_time(200, 0, 1000)
    robot.turn(45)
    levante(time/1000)
quinta()
