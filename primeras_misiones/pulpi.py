#!/usr/bin/env pybricks-micropython
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
med1_motor = Motor(Port.B)
med2_motor = Motor(Port.C)
sensor = GyroSensor(Port.S2)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 68.8, axle_track = 123)

#Realizamos una funcion que maneja el sensor de giro
def gyroMove(distance, speed):
    tg = sensor.angle()
    gain = 2
    robot.reset()
    
    while robot.distance() < distance: 
        correction = tg + sensor.angle() 
        turn_power = correction*gain
        robot.drive(speed, turn_power)

def salida_uno():
    #Mision 10: Planta de energia (25 puntos)
    robot.straight(490)
    med2_motor.run_time(-600, 400)
    robot.turn(5)
    robot.drive_time(200, 0, 200)
    med2_motor.run_time(600, 400)
    robot.drive_time(-200, 0, 200)
    med2_motor.run_time(-700, 500)
    robot.straight(100)
    sleep(0.5)
    robot.drive_time(-300, 0, 2500)
    
def salida_dos():
    #Mision 8: Television (20 puntos)
    ev3.speaker.beep()
    robot.drive_time(180, 0, 2200)
    robot.drive_time(-200, 0, 1450)

    #Mision 7: Turbina eolica (30 puntos)
    robot.turn(-65)
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

def salida_tres():
    #Mision 6: Auto hibrido (20 puntos + pila recargable (dino))
    med2_motor.run_time(300, 700)
    gyroMove(800, 200)
    robot.turn(15)
    med2_motor.run_time(-300, 600)
    sleep(0.5)
    med2_motor.run_time(300, 600)

    #Regreso del robot al area home
    robot.drive_time(-500,0, 3000)
    robot.drive_time()

def salida_cuatro():
    #Mision 14: Fabrica de juguetes(20 puntos)
    ev3.speaker.beep()
    robot.drive_time(220, 0, 950)
    med1_motor.run_time(-25,3000)
    med1_motor.run_time(100,1500)

    #Mision 9: Dino(30 puntos)
    robot.straight(-130)
    robot.turn(-70)
    sleep(0.5)
    robot.drive_time(400, 0, 10000)

def salida_cinco():
    #Mision 3: Almacenamiento de energia(30 puntos)
    robot.drive_time(300, 0, 1110)
    robot.turn(60)
    robot.drive_time(200, 0, 1800)
    robot.turn(-90)
    med2_motor.run_time(100, 1100)
    sleep(0.5)
    med2_motor.run_time(-100, 1100)

    #Mision 4: Granja Solar(20 puntos)
    robot.turn(80)
    robot.drive_time(200, 0, 1200)
    robot.turn(70)
    robot.drive_time(200, 0, 800)

    #Mision 5: Red inteligente(manito)(20 o el mejor caso 30 puntos)
    robot.turn(80)
    med1_motor.run_time(-200, 600)
    robot.turn(-90)
    med1_motor.run_time(200, 600)

    #Mision 13: Power-to-x(15)
    robot.drive_time(-1,0,50)
    robot.turn(120)
    robot.drive_time(200, 0, 1500)
    robot.turn(20)

#Aqui corremos la ev3
while True:
    
    if Button.LEFT in ev3.buttons.pressed():
        ev3.speaker.beep()
        salida_uno()
    if  Button.RIGHT in ev3.buttons.pressed():
        ev3.speaker.beep()
        salida_dos()
    if Button.UP in ev3.buttons.pressed():
        ev3.speaker.beep()
        salida_tres()
    if Button.DOWN in ev3.buttons.pressed():
        ev3.speaker.beep()
        salida_cuatro()
    if Button.CENTER in ev3.buttons.pressed():
        ev3.speaker.beep()
        salida_cinco()
