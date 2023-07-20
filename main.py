#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
#Inicializacion de objetos

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
sensor = GyroSensor(Port.S2)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 68.8, axle_track = 123)

def gyroMove(distance, speed):
    tg = sensor.angle()
    gain = 2
    robot.reset()
    
    while robot.distance() < distance: 
        correction = tg + sensor.angle() 
        turn_power = correction*gain
        robot.drive(speed, turn_power)

gyroMove(10000,100)

def gyro_reset():
    sensor.reset_angle(0)
    while True:
        if sensor.angle() == 0:
            break
    while True:
        if sensor.speed() == 0:
            break


def gyroTurn(grados):
    gyro_reset()
    sensor.reset_angle(0)
    
    while sensor.angle() < grados:
        left_motor.run(-100)
    left_motor.stop()


def derecha(grados):
    gyro_reset()
    sensor.reset_angle(0)
    
    while sensor.angle() > (-grados):
        left_motor.run(100)
    left_motor.stop()




