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
colors_enemy = (Color.BLUE, Color.YELLOW, Color.RED) 
#Constants
turns = 6
nslots = 6
#Robot
bot_hp = 750
bot_energy = 500
#Attacks
crane_damage = 200
touch_damage = 100
sound_damage = 50
crane_consume = 300
touch_consume = 150
sound_consume = 50
#Cures
cure1_recovered_hp = 100
cure2_recovered_hp = 200
cure3_recovered_hp = 400
cure1_consume = 200
cure2_consume = 300
cure3_consume = 400
#Enemies
tank_force = 200
artillery_force = 500
infantry_force = 100
tank_nr_attacks = 2
artillery_nr_attacks = 1
infantry_nr_attacks = 3
tank_hp = 200
artillery_hp = 50
infantry_hp = 100

#Defining functions_______________________________

def Scan() :
    while True:
        robot.drive(0,-1000)
        if ((UltrasonicSensor_in_1.distance() < r) or (UltrasonicSensor_in_1.distance() < min_dist) or (ColorSensor_in_2.color() in colors_enemy)):
            robot.stop()
            break

def GoToEnemy() :
    while True: 
        robot.drive(1000,0)
        if ((UltrasonicSensor_in_1.distance() > r) or (UltrasonicSensor_in_1.distance() < min_dist) or (ColorSensor_in_2.color() in colors_enemy)):
            robot.stop()
            break

def touch_atack() :
    robot.drive(-1000,0)
    robot.straight(-100)
    robot.turn(180)
    robot.straight(-100)
    robot.straight(100)
    robot.stop()
    robot.turn(180)

def crane_atack() :
    robot.drive(-1000,0)
    sleep(0.5)
    robot.stop()
    crane_motor_out_a.run_target(1000, 360*5)
    robot.turn(-90)
    robot.stop()
    robot.turn(90)
    robot.stop()
    crane_motor_out_a.run_target(1000, 360*5)

#_________________________________________________



#Defining Classes________________________________
class Defender() :
    hp = 750
    energy = 500

    def info(self) :
        print("______________________")
        print("_____DEFENDER-BOT_____\n")
        print("HP : " + str(self.hp))
        print("ENERGY : " + str(self.energy))
        print("\n\n")
        print("______________________")

    class Attack() :
        damage = 0
        consumption = 0

        def __init__(self, damage, consumption) :
            self.damage = damage
            self.consumption = consumption

        def do(self, enemy) :
            print("Damaged the Enemy with")
            enemy.hp -= self.damage

        def info(self) :
            print("______________________")
            print("_____ATTACK_____\n")
            print("DAMAGE : " + str(self.damage))
            print("CONSUMPTION : " + str(self.consumption))
            print("\n\n")
        print("______________________")

    class Cure() :
        recovered_life = 0
        consumption = 0

        def __init__(self, recovered_life, consumption) :
            self.recovered_life = recovered_life
            self.consumption = consumption

class Enemy() :
    hp = 0
    strenght = 0
    nr_of_attacks = 0
    impact_attack = 0
    def __init__(self, hp, strenght, nr_of_attacks) :
        self.strenght = strenght
        self.nr_of_attacks = nr_of_attacks
        self.hp = hp
        self.impact_attack = hp/strenght
    
    def info(self) :
        print("______________________")
        print("_____ENEMY_____\n")
        print("HP : " + str(self.hp))
        print("STRENGHT : " + str(self.strenght))
        print("NR_OF_ATTACKS : " + str(self.nr_of_attacks))
        print("IMPACT ATTACK : " + "I/A Formula needed")
        print("\n\n")
        print("______________________")

#_________________________________________________________________________________

# Write your program here.

def main():

    #Defining all attacks, cures and enemies

    ev3.speaker.say("Program Started")

    Defender_Bot = Defender()

    Crane_Attack = Defender_Bot.Attack(crane_damage, crane_consume)
    Touch_Attack = Defender_Bot.Attack(touch_damage, touch_consume)
    Sound_Attack = Defender_Bot.Attack(sound_damage, sound_consume)

    Cure_1 = Defender_Bot.Cure(cure1_recovered_hp, cure1_consume)
    Heal_2 = Defender_Bot.Cure(cure2_recovered_hp, cure2_consume)
    Heal_3 = Defender_Bot.Cure(cure3_recovered_hp, cure3_consume)

    Tank = Enemy( tank_hp, tank_force, tank_nr_attacks)
    Artillery = Enemy(artillery_hp, artillery_force, artillery_nr_attacks)
    Infantry = Enemy(infantry_hp, infantry_force, infantry_nr_attacks)
    #________________________________________________________________

    #Begin your code here________________________________________
    print("Hello World!")
    #____________________________________________________________

#MAIN FUNCTION
if __name__ == '__main__':
   main()