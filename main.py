#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from globals import *
from brains import *

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
robot.settings(vars['straight_speed'], vars['straight_acceleration'], vars['turn_rate'], vars['turn_acceleration'])

#Initialise variables
colors_enemy = (Color.BLUE, Color.YELLOW, Color.RED)

#Flags
colorDetected = False
enemyDetected = False

#Defining functions_______________________________
def Scan() : 
    global enemyDetected
    
    if enemyDetected == False :
        while UltrasonicSensor_in_1.distance() > vars['r']:
            robot.drive(0, -vars['turn_rate'])
        else:
            enemyDetected = True
            # print("EnemyDetected")
            
def LoseEnemy():
    global enemyDetected
    if enemyDetected == True:
        while UltrasonicSensor_in_1.distance() < vars['r']:
            robot.drive(0, -vars['turn_rate'])
        else:
            # print("EnemyLosed")
            enemyDetected = False
            
def CountEnemies() :
    global enemyDetected, accumulated_angle
    vars['enemies'] = 0
    vars['enemies_positions'].clear()
    vars['enemies_distances'].clear()
    GyroSensor_in_3.reset_angle(0)
    
    if UltrasonicSensor_in_1.distance() < vars['r']:
        enemyDetected = True
    
    while GyroSensor_in_3.angle() > -360 and vars['enemies'] < vars['enemies_total']:
        LoseEnemy()
        Scan()
        if enemyDetected == True:
            vars['enemies'] += 1
            vars['enemies_positions'].append(GyroSensor_in_3.angle())
            vars['enemies_distances'].append(UltrasonicSensor_in_1.distance())
            print("Slot # :" + str(vars['enemies']) + " found on :" + str(GyroSensor_in_3.angle()) + "° at :" + str(UltrasonicSensor_in_1.distance()/10) +"cm")
    
    print("Bot found " + str(vars['enemies']) + " enemies")
    accumulated_angle = GyroSensor_in_3.angle()
    robot.stop()
    
def GoToEnemy(slot):
    global recorded_moves
    slot -= 1
    GyroSensor_in_3.reset_angle(0)
    robot.turn(vars['enemies_positions'][slot]-accumulated_angle-15)
    while colorDetected == False:
        if UltrasonicSensor_in_1.distance() > vars['enemies_distances'][slot] :
            robot.drive(0, -vars['turn_rate'])
        if UltrasonicSensor_in_1.distance() > vars['min_dist'] and UltrasonicSensor_in_1.distance() < vars['enemies_distances'][slot] :
            robot.drive(vars['straight_speed'], 0)
        elif UltrasonicSensor_in_1.distance() < vars['min_dist'] :
            robot.stop()
            if ColorSensor_in_2.color() not in colors_enemy :
                robot.drive(0, -50)
            else :
                print(ColorSensor_in_2.color())
                break
            
def GetBack(slot):
    while True:
        robot.turn(-180)
        robot.straight(vars['enemies_distances'][slot]*12.5)
        robot.turn(-(vars['enemies_positions'][slot]))
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
    


def main():

    #Defining all attacks, cures and enemies
    Defender_Bot = Defender()

    Crane_Attack = Defender_Bot.Attack('Crane', vars['crane_damage'], vars['crane_consume'])
    Touch_Attack = Defender_Bot.Attack('Touch', vars['touch_damage'], vars['touch_consume'])
    Sound_Attack = Defender_Bot.Attack('Sound', vars['sound_damage'], vars['sound_consume'])

    Cure_1 = Defender_Bot.Cure('Cure1', vars['cure1_recovered_hp'], vars['cure1_consume'])
    Heal_2 = Defender_Bot.Cure('Cure2', vars['cure2_recovered_hp'], vars['cure2_consume'])
    Heal_3 = Defender_Bot.Cure('Cure3', vars['cure3_recovered_hp'], vars['cure3_consume'])
    
    #________________________________________________________________
        
    CountEnemies()
    time.sleep(2)
    

if __name__ == '__main__' :
    main()
    CountEnemies()
    GoToEnemy(1)