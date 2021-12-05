import tkinter as tk
from brains import *
# import main
import importlib

root = tk.Tk()

window_width = 800
window_height = 600
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.title("Defender_Bot : Control Panel")
# root.iconbitmap('./remote.ico')
root.resizable(False, False)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#######################################__________________VARIABLES________________________############################################
vars = {
    'bot_hp' : 750,
    'bot_energy' : 500,
    'crane_damage' : 200,
    'crane_consume' : 300,
    'touch_damage' : 100, 
    'touch_consume' : 150,
    'sound_damage' : 50, 
    'sound_consume' : 50, 
    'cure1_recovered_hp' : 100,
    'cure1_consume' : 200, 
    'cure2_recovered_hp' : 200,
    'cure2_consume' : 300,
    'cure3_recovered_hp' : 400,
    'cure3_consume' : 400,
    'tank_hp' : 200,
    'tank_force' : 200,
    'tank_nr_attacks' : 2,
    'artillery_hp' : 50,
    'artillery_force' : 500,
    'artillery_nr_attacks' : 1,
    'infantry_hp' : 100,
    'infantry_force' : 100,
    'infantry_nr_attacks' : 3,
    'min_dist': 40,
    'r' : 450,
    'straight_speed' : 200,
    'straight_acceleration' : 100,
    'turn_rate' : 100,
    'turn_acceleration' : 100,
    'enemies' : 0,
    'enemies_total' : 6,
    'gameStarted' : False,
    'enemy_slots' : [],
    'enemies_positions' : [],
    'enemies_distances' : []
}
#_________IntVars_________
bot_hp_var = IntVar(value=vars['bot_hp'])
bot_energy_var = IntVar(value=vars['bot_energy'])

crane_damage_var = IntVar(value=vars['crane_damage'])
crane_consume_var = IntVar(value=vars['crane_consume'])

touch_damage_var = IntVar(value=vars['touch_damage'])
touch_consume_var = IntVar(value=vars['touch_consume'])

sound_damage_var = IntVar(value=vars['sound_damage'])
sound_consume_var = IntVar(value=vars['sound_consume'])

cure1_recovered_hp_var = IntVar(value=vars['cure1_recovered_hp'])
cure1_consume_var = IntVar(value=vars['cure1_consume'])

cure2_recovered_hp_var = IntVar(value=vars['cure2_recovered_hp'])
cure2_consume_var = IntVar(value=vars['cure2_consume'])

cure3_recovered_hp_var = IntVar(value=vars['cure3_recovered_hp'])
cure3_consume_var = IntVar(value=vars['cure3_consume'])

tank_hp_var = IntVar(value=vars['tank_hp'])
tank_force_var = IntVar(value=vars['tank_force'])
tank_nr_attacks_var = IntVar(value=vars['tank_nr_attacks'])

artillery_hp_var = IntVar(value=vars['artillery_hp'])
artillery_force_var = IntVar(value=vars['artillery_force'])
artillery_nr_attacks_var = IntVar(value=vars['artillery_nr_attacks'])

infantry_hp_var = IntVar(value=vars['infantry_hp'])
infantry_force_var = IntVar(value=vars['infantry_force'])
infantry_nr_attacks_var = IntVar(value=vars['infantry_nr_attacks'])

min_dist_var = IntVar(value=vars['min_dist'])
r_var = IntVar(value=vars['r'])
straight_speed_var = IntVar(value=vars['straight_speed'])
straight_acceleration_var = IntVar(value=vars['straight_acceleration'])
turn_rate_var = IntVar(value=vars['turn_rate'])
turn_acceleration_var = IntVar(value=vars['turn_acceleration'])




#Creating functions for onchange
def bot_hp_change(var, indx, mode) :
    vars['bot_hp'] = bot_hp_entry.get()
def bot_energy_change(var, indx, mode) :
    vars['bot_energy'] = bot_energy_entry.get() 

def crane_damage_change(var, indx, mode) :
    vars['crane_damage'] = crane_damage_entry.get() 
def crane_consume_change(var, indx, mode) :
    vars['crane_consume'] = crane_consume_entry.get() 

def touch_damage_change(var, indx, mode) :
    vars['touch_damage'] = touch_damage_entry.get() 
def touch_consume_change(var, indx, mode) :
    vars['touch_consume'] = touch_consume_entry.get() 

def sound_damage_change(var, indx, mode) :
    vars['sound_damage'] = sound_damage_entry.get() 
def sound_consume_change(var, indx, mode) :
    vars['sound_consume'] = sound_consume_entry.get() 
    
def cure1_recovered_hp_change(var, indx, mode) :
    vars['cure1_recovered_hp'] = cure1_recovered_hp_entry.get() 
def cure1_consume_change(var, indx, mode) :
    vars['cure1_consume'] = cure1_consume_entry.get() 
    
def cure2_recovered_hp_change(var, indx, mode) :
    vars['cure2_recovered_hp'] = cure2_recovered_hp_entry.get() 
def cure2_consume_change(var, indx, mode) :
    vars['cure2_consume'] = cure2_consume_entry.get() 

def cure3_recovered_hp_change(var, indx, mode) :
    vars['cure3_recovered_hp'] = cure3_recovered_hp_entry.get() 
def cure3_consume_change(var, indx, mode) :
    vars['cure3_consume'] = cure3_consume_entry.get() 

def tank_hp_change(var, indx, mode) :
    vars['tank_hp'] = tank_hp_entry.get() 
def tank_force_change(var, indx, mode) :
    vars['tank_force'] = tank_force_entry.get() 
def tank_nr_attacks_change(var, indx, mode) :
    vars['tank_nr_attacks'] = tank_nr_attacks_entry.get() 

def artillery_hp_change(var, indx, mode) :
    vars['artillery_hp'] = artillery_hp_entry.get() 
def artillery_force_change(var, indx, mode) :
    vars['artillery_force'] = artillery_force_entry.get() 
def artillery_nr_attacks_change(var, indx, mode) :
    vars['artillery_nr_attacks'] = artillery_nr_attacks_entry.get() 

def min_dist_change(var, indx, mode) :
    vars['min_dist'] = min_dist_entry.get() 
def infantry_hp_change(var, indx, mode) :
    vars['infantry_hp'] = infantry_hp_entry.get() 
def infantry_force_change(var, indx, mode) :
    vars['infantry_force'] = infantry_force_entry.get() 
def infantry_nr_attacks_change(var, indx, mode) :
    vars['infantry_nr_attacks'] = infantry_nr_attacks_entry.get() 
def r_change(var, indx, mode) :
    vars['r'] = r_entry.get() 
def straight_speed_change(var, indx, mode) :
    vars['straight_speed'] = straight_speed_entry.get() 
def straight_acceleration_change(var, indx, mode) :
    vars['straight_acceleration'] = straight_acceleration_entry.get() 
def turn_rate_change(var, indx, mode) :
    vars['turn_rate'] = turn_rate_entry.get() 
def turn_acceleration_change(var, indx, mode) :
    vars['turn_acceleration'] = turn_acceleration_entry.get() 

def start_program() :
    # importlib.reload(main)
    print('Program was started! ')
    print("Bot_HP now is " + str(vars['bot_hp']))

def stop_program() :
    vars['getStarted'] = False

#Add traces for onchange events
bot_hp_var.trace_add('write', bot_hp_change)
bot_energy_var.trace_add('write', bot_energy_change)
crane_damage_var.trace_add('write', crane_damage_change)
crane_consume_var.trace_add('write', crane_consume_change)
touch_damage_var.trace_add('write', touch_damage_change)
touch_consume_var.trace_add('write', touch_consume_change)
sound_damage_var.trace_add('write', sound_damage_change)
sound_consume_var.trace_add('write', sound_consume_change)
cure1_recovered_hp_var.trace_add('write', cure1_recovered_hp_change)
cure1_consume_var.trace_add('write', cure1_consume_change)
cure2_recovered_hp_var.trace_add('write', cure2_recovered_hp_change)
cure2_consume_var.trace_add('write', cure2_consume_change)
cure3_recovered_hp_var.trace_add('write', cure3_recovered_hp_change)
cure3_consume_var.trace_add('write', cure3_consume_change)
tank_hp_var.trace_add('write', tank_hp_change)
tank_force_var.trace_add('write', tank_force_change)
tank_nr_attacks_var.trace_add('write', tank_nr_attacks_change)
artillery_hp_var.trace_add('write', artillery_hp_change)
artillery_force_var.trace_add('write', artillery_force_change)
artillery_nr_attacks_var.trace_add('write', artillery_nr_attacks_change)
infantry_hp_var.trace_add('write', infantry_hp_change)
infantry_force_var.trace_add('write', infantry_force_change)
infantry_nr_attacks_var.trace_add('write', infantry_nr_attacks_change)

min_dist_var.trace_add('write', min_dist_change)
r_var.trace_add('write', r_change)
straight_speed_var.trace_add('write', straight_speed_change)
straight_acceleration_var.trace_add('write', straight_acceleration_change)
turn_rate_var.trace_add('write', turn_rate_change)
turn_acceleration_var.trace_add('write', turn_acceleration_change)

#######################################______________CREATING_____________________##############################################
#LabelFrames creating
bot_label_frame = tk.LabelFrame(root, text='Defender')
bot_frame = tk.LabelFrame(bot_label_frame, text='Bot')

bot_attacks_frame = tk.LabelFrame(bot_label_frame, text='Attacks', bg='red')
crane_frame = tk.LabelFrame(bot_attacks_frame, text='Crane')
touch_frame = tk.LabelFrame(bot_attacks_frame, text='Touch')
sound_frame = tk.LabelFrame(bot_attacks_frame, text='Sound')

cures_label_frame = tk.LabelFrame(bot_label_frame, text='Cures', bg='blue')
cure1_frame = tk.LabelFrame(cures_label_frame, text='Cure 1')
cure2_frame = tk.LabelFrame(cures_label_frame, text='Cure 2')
cure3_frame = tk.LabelFrame(cures_label_frame, text='Cure 3')

parent_frame = tk.Frame(root)
enemies_label_frame = tk.LabelFrame(parent_frame, text='Enemies')
tank_frame = tk.LabelFrame(enemies_label_frame, text='Tank')
art_frame = tk.LabelFrame(enemies_label_frame, text='Artillery')
inf_frame = tk.LabelFrame(enemies_label_frame, text='Infantry')

other_label_frame = tk.LabelFrame(parent_frame, text="Other")


#________________LABELS CREATE___________________

#Bot______________________________

bot_hp_label = Label(bot_frame, text="Bot-HP")
bot_energy_label = Label(bot_frame, text='Bot-Energy')

#Attacks____________________________

#Crane
crane_damage_label = Label(crane_frame, text='Crane-Damage')
crane_consume_label = Label(crane_frame, text='Crane-Consume')
#Touch
touch_damage_label = Label(touch_frame, text='Touch-Damage')
touch_consume_label = Label(touch_frame, text='Touch-Consume')
#Sound
sound_damage_label = Label(sound_frame, text='Sound-Damage')
sound_consume_label = Label(sound_frame, text='Sound-Consume')

#Cures____________________________________

#Cure1
cure1_recovered_hp_label = Label(cure1_frame, text='Cure1-RecoveredHP')
cure1_consume_label = Label(cure1_frame, text='Cure1-Consume')
#Cure2
cure2_recovered_hp_label = Label(cure2_frame, text='Cure2-RecoveredHP')
cure2_consume_label = Label(cure2_frame, text='Cure2-Consume')
#Cure3
cure3_recovered_hp_label = Label(cure3_frame, text='Cure3-RecoveredHP')
cure3_consume_label = Label(cure3_frame, text='Cure3-Consume')

#Enemies_________________________________

#Tank
tank_hp_label = Label(tank_frame, text='Tank-HP')
tank_force_label = Label(tank_frame, text='Tank-Force')
tank_nr_attacks_label = Label(tank_frame, text='Tank-Attacks#')
#Artillery
artillery_hp_label = Label(art_frame, text='Artillery-HP')
artillery_force_label = Label(art_frame, text='Artillery-Force')
artillery_nr_attacks_label = Label(art_frame, text='Artillery-Attacks#')
#Infantry
infantry_hp_label = Label(inf_frame, text='Infantry-HP')
infantry_force_label = Label(inf_frame, text='Infantry-Force')
infantry_nr_attacks_label = Label(inf_frame, text='Infantry-Attacks#')

#Other

min_dist_label = Label(other_label_frame, text='Minimal-Distance')
r_label = Label(other_label_frame, text='Radius')
straight_speed_label = Label(other_label_frame, text='Straight-Speed')
straight_acceleration_label = Label(other_label_frame, text='Straight-Acceleration')
turn_rate_label = Label(other_label_frame, text='Turn-Rate')
turn_acceleration_label = Label(other_label_frame, text='Turn-Acceleration')


#______________Entries Create_____________
bot_hp_entry = Entry(bot_frame, justify=CENTER, textvariable=bot_hp_var)
bot_energy_entry = Entry(bot_frame, justify=CENTER, textvariable=bot_energy_var)

crane_damage_entry = Entry(crane_frame, justify=CENTER, textvariable=crane_damage_var)
crane_consume_entry = Entry(crane_frame, justify=CENTER, textvariable=crane_consume_var)

touch_damage_entry = Entry(touch_frame, justify=CENTER, textvariable=touch_damage_var)
touch_consume_entry = Entry(touch_frame, justify=CENTER, textvariable=touch_consume_var)

sound_damage_entry = Entry(sound_frame, justify=CENTER, textvariable=sound_damage_var)
sound_consume_entry = Entry(sound_frame, justify=CENTER, textvariable=sound_consume_var)

cure1_recovered_hp_entry = Entry(cure1_frame, justify=CENTER, textvariable=cure1_recovered_hp_var)
cure1_consume_entry = Entry(cure1_frame, justify=CENTER, textvariable=cure1_consume_var)

cure2_recovered_hp_entry = Entry(cure2_frame, justify=CENTER, textvariable=cure2_recovered_hp_var)
cure2_consume_entry = Entry(cure2_frame, justify=CENTER, textvariable=cure2_consume_var)

cure3_recovered_hp_entry = Entry(cure3_frame, justify=CENTER, textvariable=cure3_recovered_hp_var)
cure3_consume_entry = Entry(cure3_frame, justify=CENTER, textvariable=cure3_consume_var)

tank_hp_entry = Entry(tank_frame, justify=CENTER, textvariable=tank_hp_var)
tank_force_entry = Entry(tank_frame, justify=CENTER, textvariable=tank_force_var)
tank_nr_attacks_entry = Entry(tank_frame, justify=CENTER, textvariable=tank_nr_attacks_var)

artillery_hp_entry = Entry(art_frame, justify=CENTER, textvariable=artillery_hp_var)
artillery_force_entry = Entry(art_frame, justify=CENTER, textvariable=artillery_force_var)
artillery_nr_attacks_entry = Entry(art_frame, justify=CENTER, textvariable=artillery_nr_attacks_var)

infantry_hp_entry = Entry(inf_frame, justify=CENTER, textvariable=infantry_hp_var)
infantry_force_entry = Entry(inf_frame, justify=CENTER, textvariable=infantry_force_var)
infantry_nr_attacks_entry = Entry(inf_frame, justify=CENTER, textvariable=infantry_nr_attacks_var)

min_dist_entry = Entry(other_label_frame, justify=CENTER, textvariable=min_dist_var)
r_entry = Entry(other_label_frame, justify=CENTER, textvariable=r_var)
straight_speed_entry = Entry(other_label_frame, justify=CENTER, textvariable=straight_speed_var)
straight_acceleration_entry = Entry(other_label_frame, justify=CENTER, textvariable=straight_acceleration_var)
turn_rate_entry = Entry(other_label_frame, justify=CENTER, textvariable=turn_rate_var)
turn_acceleration_entry = Entry(other_label_frame, justify=CENTER, textvariable=turn_acceleration_var)

#Create Buttons 
start_button = Button(parent_frame, text='Start Program', command=start_program)
stop_button = Button(parent_frame, text='Stop Program', command=stop_program)

######################################################_________________DISPLAYING_______________#####################################################################
#Labels display
bot_hp_label.grid(sticky='W', column='0', row='0')
bot_energy_label.grid(sticky='W', column='0', row='1')

crane_damage_label.grid(sticky='W', column='0', row='2')
crane_consume_label.grid(sticky='W', column='0', row='3')

touch_damage_label.grid(sticky='W', column='0', row='4')
touch_consume_label.grid(sticky='W', column='0', row='5')

sound_damage_label.grid(sticky='W', column='0', row='6')
sound_consume_label.grid(sticky='W', column='0', row='7')

cure1_recovered_hp_label.grid(sticky='W', column='0', row='8')
cure1_consume_label.grid(sticky='W', column='0', row='9')

cure2_recovered_hp_label.grid(sticky='W', column='0', row='10')
cure2_consume_label.grid(sticky='W', column='0', row='11')

cure3_recovered_hp_label.grid(sticky='W', column='0', row='12')
cure3_consume_label.grid(sticky='W', column='0', row='13')

tank_hp_label.grid(sticky='W', column='0', row='14')
tank_force_label.grid(sticky='W', column='0', row='15')
tank_nr_attacks_label.grid(sticky='W', column='0', row='16')

artillery_hp_label.grid(sticky='W', column='0', row='17')
artillery_force_label.grid(sticky='W', column='0', row='18')
artillery_nr_attacks_label.grid(sticky='W', column='0', row='19')

infantry_hp_label.grid(sticky='W', column='0', row='20')
infantry_force_label.grid(sticky='W', column='0', row='21')
infantry_nr_attacks_label.grid(sticky='W', column='0', row='22')

min_dist_label.grid(sticky='W', column='0', row='23')
r_label.grid(sticky='W', column='0', row='24')
straight_speed_label.grid(sticky='W', column='0', row='25')
straight_acceleration_label.grid(sticky='W', column='0', row='26')
turn_rate_label.grid(sticky='W', column='0', row='27')
turn_acceleration_label.grid(sticky='W', column='0', row='28')

#Entries Display
bot_hp_entry.grid(sticky='W', column='1', row='0')
bot_energy_entry.grid(sticky='W', column='1', row='1')

crane_damage_entry.grid(sticky='W', column='1', row='2')
crane_consume_entry.grid(sticky='W', column='1', row='3')

touch_damage_entry.grid(sticky='W', column='1', row='4')
touch_consume_entry.grid(sticky='W', column='1', row='5')

sound_damage_entry.grid(sticky='W', column='1', row='6')
sound_consume_entry.grid(sticky='W', column='1', row='7')

cure1_recovered_hp_entry.grid(sticky='W', column='1', row='8')
cure1_consume_entry.grid(sticky='W', column='1', row='9')

cure2_recovered_hp_entry.grid(sticky='W', column='1', row='10')
cure2_consume_entry.grid(sticky='W', column='1', row='11')

cure3_recovered_hp_entry.grid(sticky='W', column='1', row='12')
cure3_consume_entry.grid(sticky='W', column='1', row='13')

tank_hp_entry.grid(sticky='W', column='1', row='14')
tank_force_entry.grid(sticky='W', column='1', row='15')
tank_nr_attacks_entry.grid(sticky='W', column='1', row='16')

artillery_hp_entry.grid(sticky='W', column='1', row='17')
artillery_force_entry.grid(sticky='W', column='1', row='18')
artillery_nr_attacks_entry.grid(sticky='W', column='1', row='19')

infantry_hp_entry.grid(sticky='W', column='1', row='20')
infantry_force_entry.grid(sticky='W', column='1', row='21')
infantry_nr_attacks_entry.grid(sticky='W', column='1', row='22')

min_dist_entry.grid(sticky='W', column='1', row='23')
r_entry.grid(sticky='W', column='1', row='24')
straight_speed_entry.grid(sticky='W', column='1', row='25')
straight_acceleration_entry.grid(sticky='W', column='1', row='26')
turn_rate_entry.grid(sticky='W', column='1', row='27')
turn_acceleration_entry.grid(sticky='W', column='1', row='28')

#Display bot frame
bot_label_frame.pack(side=LEFT, pady=5)
bot_frame.pack()
#attacks frame
bot_attacks_frame.pack(fill='both')
crane_frame.pack(pady=9, fill='both')
touch_frame.pack(pady=9, fill='both')
sound_frame.pack(pady=9, fill='both')
#cures frame
cures_label_frame.pack(fill='both')
cure1_frame.pack(pady=9, fill='both')
cure2_frame.pack(pady=9, fill='both')
cure3_frame.pack(pady=9, fill='both')
#parent frame
parent_frame.pack(side=LEFT)
#enemies frame
enemies_label_frame.pack(fill='both')
tank_frame.pack(pady=9, fill='both')
art_frame.pack(pady=9, fill='both')
inf_frame.pack(pady=9, fill='both')
#other 
other_label_frame.pack()

#buttons
start_button.pack(side=BOTTOM)
stop_button.pack(side=BOTTOM)


def main():

    #Defining all attacks, cures and enemies
    vars['gameStarted'] = True
    if vars['gameStarted'] == True :

        Defender_Bot = Defender()

        Crane_Attack = Defender_Bot.Attack('Crane', vars['crane_damage'], vars['crane_consume'])
        Touch_Attack = Defender_Bot.Attack('Touch', vars['touch_damage'], vars['touch_consume'])
        Sound_Attack = Defender_Bot.Attack('Sound', vars['sound_damage'], vars['sound_consume'])

        Cure_1 = Defender_Bot.Cure('Cure1', vars['cure1_recovered_hp'], vars['cure1_consume'])
        Heal_2 = Defender_Bot.Cure('Cure2', vars['cure2_recovered_hp'], vars['cure2_consume'])
        Heal_3 = Defender_Bot.Cure('Cure3', vars['cure3_recovered_hp'], vars['cure3_consume'])
        
        #________________________________________________________________
        
        print('Bot - hp ' + str(vars['bot_hp']))
        print('Game started = '+ str(vars['gameStarted']))

    else :
        print('Game started = '+ str(vars['gameStarted']))
        quit()

if __name__ == '__main__' :
    main()
    root.mainloop()