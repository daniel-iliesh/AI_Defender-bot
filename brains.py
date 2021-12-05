import random
from tkinter import *
from tkinter.ttk import *
from random import randint

#Functions            
    
def ChooseYourDestiny() : 
    global aux_enemy
        
    generated_order = random.sample(range(6), 6)
    print(generated_order)

    for x in range(6) :
        ThrowDice1()
        dice2 = generated_order[x]
        vars['enemy_slots'].insert(dice2, aux_enemy)
        print("Inserted " + str(aux_enemy) + " it will attack " + str(dice2))
        
    print("EnemySlots :----  " + str(vars['enemy_slots']))

#Classes
class Defender() :

    def info(self) :
        print("______________________")
        print("_____DEFENDER-BOT_____\n")
        print("HP : " + str(bot_hp))
        print("ENERGY : " + str(bot_energy))
        print("\n\n")
        print("______________________")

    class Attack() :
        name = ''
        damage = 0
        consumption = 0

        def __init__(self,name, damage, consumption) :
            self.name = name
            self.damage = damage
            self.consumption = consumption

        def do(self, enemy) :
            print("Damaged the Enemy with")
            enemy.hp -= self.damage
            vars['bot_energy'] -= self.consumption

        def info(self) :
            print("______________________")
            print("_____ATTACK_____\n")
            print('NAME : ' + self.name)
            print("DAMAGE : " + str(self.damage))
            print("CONSUMPTION : " + str(self.consumption))
            print("\n\n")
        print("______________________")
            
    class Cure() :
        name = ''
        recovered_life = 0
        consumption = 0

        def __init__(self,name, recovered_life, consumption) :
            self.name = name
            self.recovered_life = recovered_life
            self.consumption = consumption

        def do(self) :
            print("Cured the Enemy with")
            vars['bot_hp'] += self.recovered_life
            vars['bot_energy'] -= self.consumption

class Enemy() :
    name = ""
    hp = 0
    strenght = 0
    nr_of_attacks = 0
    impact_attack = 0

    def __init__(self, name,  hp, strenght, nr_of_attacks) :
        self.name = name
        self.strenght = strenght
        self.nr_of_attacks = nr_of_attacks
        self.hp = hp
        self.impact_attack = int(hp)/int(strenght)
    
    def info(self) :
        print("______________________")
        print("_____ENEMY_____\n")
        print("Name : " + self.name)
        print("HP : " + str(self.hp))
        print("STRENGHT : " + str(self.strenght))
        print("NR_OF_ATTACKS : " + str(self.nr_of_attacks))
        print("IMPACT ATTACK : " + "I/A Formula needed")
        print("\n\n")
        print("______________________")

    def isAttacking(self) :
        global bot_hp

        bot_hp -= self.strenght
        self.nr_of_attacks -= 1

def ThrowDice1() :
    global aux_enemy, Tank, Art, Inf

    generated_order = random.sample(range(6), 6)

    for x in range(6) :
        dice1 = randint(1, 6)
        if (dice1 == 1) or (dice1 == 2)  :
            aux_enemy = Enemy("Tank", vars['tank_hp'], vars['tank_force'], vars['tank_nr_attacks'])
        elif (dice1 == 3) or (dice1 == 4) :
            aux_enemy = Enemy("Art", vars['artillery_hp'], vars['artillery_force'], vars['artillery_nr_attacks'])
        elif (dice1 == 5) or (dice1 == 6) :
            aux_enemy = Enemy("Inf", vars['infantry_hp'], vars['infantry_force'], vars['infantry_nr_attacks'])
        vars['enemy_slots'].insert(x, aux_enemy)

def stop_program() :
    quit()

