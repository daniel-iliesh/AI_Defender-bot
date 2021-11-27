#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
UltrasonicSensor_in_1 = UltrasonicSensor(Port.S1)
ColorSensor_in_2 = ColorSensor(Port.S2) 
GyroSensor_in_3 = GyroSensor(Port.S3)
TouchSensor_in_4 = TouchSensor(Port.S4)

#Initialise Motors
crane_motor_out_a = Motor(Port.A)
left_motor_out_b = Motor(Port.B)
right_motor_out_c = Motor(Port.C)

#Initialise DriveBase
robot = DriveBase(left_motor_out_b, right_motor_out_c, wheel_diameter=35, axle_track=175)
robot.settings(straight_speed = 500, straight_acceleration = 500, turn_rate = 1000, turn_acceleration = 1000)

#Initialise variables
min_dist = 40
r = 450
turn = 1000
direction = 1000

#Define functions
def SensorValues() :
    while True:
        distance = UltrasonicSensor_in_1.distance()
        print("Distance - " + distance)
        color = ColorSensor_in_2.color()
        print("Color - " + color)

def Scan() :
    while distance > r:
        ev3.speaker.say("Not Detected")
        robot.drive(0,-turn)
    ev3.speaker.say("Detected")
    robot.stop()
    GoToEnemy()

def GoToEnemy() :
    while color == Color.BLACK or None :
        while (distance > min_dist) and (distance < r) :
            robot.drive(direction)
        Scan()
    robot.stop()

class Defender() :
    hp = 750
    energy = 500

    class Attack() :
        damage = 0
        consumption = 0

        def __init__(self, damage, consumption) :
            self.damage = damage
            self.consumption = consumption

    class Cure() :
        recovered_life = 0
        consumption = 0

        def __init__(self, recovered_life, consumption) :
            self.recovered_life = recovered_life
            self.consumption = consumption

class Enemy() :
    name = str("")
    hp = 0
    strenght = 0
    nr_of_attacks = 0
    impact_attack = 0
        def __init__(self, name, hp, strenght, nr_of_attacks, impact_attack)
            self.name = name
            self.strenght = strenght
            self.nr_of_attacks = nr_of_attacks
            self.hp = hp
            self.impact_attack = impact_attack
# Write your program here.
ev3.speaker.say("Program Started")

Crane_Attack = Attack(200, 300)
Touch_Attack = Attack(100, 150)
Sound_Attack = Attack(50, 50)

Cure_1 = Cure(100, 200)
Heal_2 = Cure(200, 300)
Heal_3 = Cure(400, 400)

Tank = Enemy("Tank", 200, 200, 2, 400)
Artillery = Enemy("Artillery", 50, 500, 1, 250)
Infantry = Enemy("Infantry", 100, 100, 3, 100)
SensorValues()
Scan()



    



        
 