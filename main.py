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


class Defender() :
    hp = 750
    energy = 500

    def info(self) :
        pr("______________________")
        pr("_____DEFENDER-BOT_____\n")
        pr("HP : " + str(self.hp))
        pr("ENERGY : " + str(self.energy))
        pr("\n\n")
        pr("______________________")


    class Attack() :
        damage = 0
        consumption = 0

        def __init__(self, damage, consumption) :
            self.damage = damage
            self.consumption = consumption

        def do(self, enemy) :
            pr("Damaged the Enemy with")
            enemy.hp -= self.damage

        def info(self) :
            pr("______________________")
            pr("_____ATTACK_____\n")
            pr("DAMAGE : " + str(self.damage))
            pr("CONSUMPTION : " + str(self.consumption))
            pr("\n\n")
        pr("______________________")

            
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
        pr("______________________")
        pr("_____ENEMY_____\n")
        pr("HP : " + str(self.hp))
        pr("STRENGHT : " + str(self.strenght))
        pr("NR_OF_ATTACKS : " + str(self.nr_of_attacks))
        pr("IMPACT ATTACK : " + str(self.name))
        pr("\n\n")
        pr("______________________")
        

def main():

    #Defining all attacks, cures and enemies

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

    Defender_Bot.info()
    Crane_Attack.info()
    Tank.info()

    Crane_Attack.do(Tank)
    Tank.info()

if __name__ == '__main__':
   main()



    



        
 