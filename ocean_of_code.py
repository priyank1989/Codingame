import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height, my_id = [int(i) for i in input().split()]
island_cells=[]
available_cells=[]
my_moved_cells=[]
initial_available_cells=[]

constant_silence_distance_possible=4


for i in range(height):
    line = input()
    for j in range(width):
        if line[j] == "x":
            island_cells.append([j,i])
        else:
            available_cells.append([j,i])

initial_available_cells=available_cells[:]

def add_my_move(x_y: list):
    global available_cells, my_moved_cells
    my_moved_cells.append(x_y)
    available_cells.remove(x_y)

def to_surface(x_y: list):
    global available_cells, my_moved_cells
    available_cells=initial_available_cells[:]
    my_moved_cells.clear()
    add_my_move(x_y)
    
def check_if_path_clear(x : int, y : int, distance : int, dirn: str) -> bool:
    if dirn in ["E", "W"]:
        iter_val=-1
        if dirn == "E":
            iter_val=1
        for i in range(x + iter_val, x + (distance*iter_val) + iter_val, iter_val):
            if [i, y] not in available_cells:
                return False
        return True
    if dirn in ["N", "S"]:
        iter_val=-1
        if dirn == "S":
            iter_val=1
        for i in range(y + iter_val, y + (distance*iter_val) + iter_val, iter_val):
            if [x, i] not in available_cells:
                return False
        return True


def possible_move(x: int, y: int, how_far=1) -> str:
    possible_moves_list={
                            "N" : [x, y-how_far],
                            "E" : [x+how_far, y],
                            "W" : [x-how_far, y],
                            "S" : [x , y+how_far]                        
                        }
    possible_moves=[]
    for key in possible_moves_list:
        if check_if_path_clear(x,y,how_far,key):
            possible_moves.append(key)
    if len(possible_moves) > 0:
        dir_choice=random.choice(possible_moves) 
        add_my_move(possible_moves_list[dir_choice])
        return dir_choice
    else:
        return None

def is_torpedo_ready(torpedo_cooldown: int) -> bool:
    return torpedo_cooldown == 0 

def is_sonar_ready(sonar_cooldown: int) -> bool:
    return sonar_cooldown == 0

def is_silence_ready(silence_cooldown: int) -> bool:
    return silence_cooldown == 0

def is_mine_ready(mine_cooldown: int) -> bool:
    return mine_cooldown == 0

def what_to_charge(torpedo_cooldown: int, sonar_cooldown: int, silence_cooldown: int, mine_cooldown: int) -> str:
    if not is_torpedo_ready(torpedo_cooldown):
        return "TORPEDO"
    elif not is_silence_ready(silence_cooldown):
        return "SILENCE"
    elif not is_sonar_ready(sonar_cooldown):
        return "SONAR"
    # elif not is_mine_ready(mine_cooldown):
    #     return "MINE"
    else:
        return ""

def run_silent(x : int, y : int):
    possible_jump=0
    silence_dir=""
    for run_length in range(2, constant_silence_distance_possible + 1):
        return_val=possible_move(x, y, run_length)
        if return_val != None:
            possible_jump=run_length
            silence_dir=return_val
        else:
            break
    if possible_jump > 0 and silence_dir != "":
        return "SILENCE {} {}".format(silence_dir, possible_jump)
    else:
        return None


def fire_torpedo(x: int, y : int):
    pass

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
[spawn_x, spawn_y] = random.choice(available_cells) 
print("{} {}".format(spawn_x, spawn_y))
add_my_move([spawn_x, spawn_y])

# game loop
while True:
    x, y, my_life, opp_life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown = [int(i) for i in input().split()]
    sonar_result = input()
    opponent_orders = input()

    print("second loop",opponent_orders, sonar_result, file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if "SURFACE" in opponent_orders:
        opponent_sector=opponent_orders.split(" ")[1]
        print("Opponent surfaced in sector {}".format(opponent_sector), file=sys.stderr)
        
    elif "TORPEDO" in opponent_orders:
        torpedo_x, torpedo_y=opponent_orders.split(" ")[1:3]
        torpedo_y=torpedo_y.split("|")[0]
        print("Opponent launched torpedo at {} {}".format(torpedo_x, torpedo_y), file=sys.stderr)
        # if is_silence_ready(silence_cooldown):
        #     run_from_torpedo=run_silent(x, y)
        #     print("Value of run_from_torpedo {}".format(run_from_torpedo), file=sys.stderr)
        #     if run_from_torpedo != None:
        #         print(run_from_torpedo)
        #         continue


    direction=possible_move(x, y)
    weapon_charge=what_to_charge(torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown)
    if direction != None:
        print("MOVE {} {}".format(direction, weapon_charge))
    elif is_silence_ready(silence_cooldown):
        can_silent=run_silent(x, y)
        if can_silent != None:
            print(can_silent)
        else:
            print("SURFACE")
            to_surface([x, y])
    else:
        print("SURFACE")
        to_surface([x, y])


