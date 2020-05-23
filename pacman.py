import sys
import math
import random

# Grab the pellets as fast as you can!

def get_eucliadian_distance(source_pos, destination_pos):
    return math.floor(math.sqrt( math.pow((source_pos[0] - destination_pos[0]), 2) + math.pow((source_pos[1] - destination_pos[1]), 2)))

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]

diagonal_distance = get_eucliadian_distance((0,0), (width, height))
NORMAL_PELLET = 1
SUPER_PELLET = 10
INVISIBLE_LOCATION = -1 
WALL = -10
VISITED = 0
grid = {}
last_known_pos = {}
for i in range(10):
    last_known_pos[i] = [(0, 0)]

collision_matrix = {
    "ROCK" : "SCISSORS",
    "SCISSORS" : "PAPER",
    "PAPER" : "ROCK"
}


def get_grid():
    for y in range(height):
        row = input()  # one line of the grid: space " " is floor, pound "#" is wall
        for x in range(len(row)):
            grid[(x, y)] = WALL if row[x] == "#" else INVISIBLE_LOCATION


def show_grid():
    for y in range(height):
        for x in range(width):
            value = grid[(x, y)]
            if value == -10:
                value ="#"
            elif value == -1:
                value = " "
            print(value, end="", file=sys.stderr)
        print(file=sys.stderr)


def calculate_possible_moves(grid):
    moves_grid = {}
    for (key, value) in grid.items():
        if value == WALL:
            continue
        pac_pos = key
        moves_counter = 0
        for y in range(height):
            possible_move = (pac_pos[0], y)
            if is_pellet_in_sight(pac_pos, possible_move, False):
                moves_counter += 1
        for x in range(width):
            possible_move = (x, pac_pos[1])
            if is_pellet_in_sight(pac_pos, possible_move, False):
                moves_counter += 1
        moves_grid[key] = moves_counter
    return moves_grid


def is_pellet_in_sight(pac_pos, pellet_pos, check_other_pacs = True):
    if pac_pos[0] == pellet_pos[0] and pac_pos[1] != pellet_pos[1]:
        changer = int((pac_pos[1] - pellet_pos[1]) / abs(pac_pos[1] - pellet_pos[1]))
        for y in range(pellet_pos[1], pac_pos[1], changer):
            if grid[(pac_pos[0],y)] == WALL or ( check_other_pacs and (pac_pos[0],y) in my_pac_locations):
                return False 
        return True
    
    if pac_pos[1] == pellet_pos[1] and pac_pos[0] != pellet_pos[0]:
        changer = int((pac_pos[0] - pellet_pos[0]) / abs(pac_pos[0] - pellet_pos[0]))
        for x in range(pellet_pos[0], pac_pos[0], changer):
            if grid[(x, pac_pos[1])] == WALL or (check_other_pacs and (x, pac_pos[1]) in my_pac_locations):
                return False 
        return True
    return False


def get_list_pellets(type_of_pellet):
    return [key for (key, value) in grid.items() if value == type_of_pellet]


def get_closest_super_pellet(pac_pos):
    ten_pellet_distance = diagonal_distance
    ten_point_pellet_list = get_list_pellets(SUPER_PELLET)
    closest_ten_pellet = pac_pos
    if len(ten_point_pellet_list) > 0:
        for pellet_pos in ten_point_pellet_list:
            pellet_distance = get_eucliadian_distance(pac_pos, pellet_pos)
            if pellet_distance < ten_pellet_distance and pellet_pos not in pac_current_moves:
                closest_ten_pellet = pellet_pos
                ten_pellet_distance = pellet_distance
    return closest_ten_pellet, ten_pellet_distance


def get_closest_normal_pellet(pac_pos, type_of_pellet, non_sight_check = False):
    one_pellet_distance = diagonal_distance
    one_point_pellet_list = get_list_pellets(type_of_pellet)
    closest_one_pellet = pac_pos
    if len(one_point_pellet_list) > 0:
        for pellet_pos in one_point_pellet_list:
            pellet_distance = get_eucliadian_distance(pac_pos, pellet_pos)
            is_pellet = is_pellet_in_sight(pac_pos, pellet_pos)
            if (non_sight_check or is_pellet) and pellet_distance < one_pellet_distance and pellet_pos not in pac_current_moves:
                closest_one_pellet = pellet_pos
                one_pellet_distance = pellet_distance
    return closest_one_pellet, one_pellet_distance
    

    
def get_closest_pellet(pac_pos):
    pellet_pos, pellet_distance = pac_pos, 0
    pellet_pos, pellet_distance = get_closest_super_pellet(pac_pos)
    if pellet_pos == pac_pos:
        pellet_pos, pellet_distance = get_closest_normal_pellet(pac_pos, NORMAL_PELLET)
    if pellet_pos == pac_pos:
        pellet_pos, pellet_distance = get_closest_normal_pellet(pac_pos, INVISIBLE_LOCATION, True)
    return pellet_pos, pellet_distance


def find_move(pac_pos, last_known_pac_pos):
    best_move_value = 0
    best_move = pac_pos
    for pos, possible_moves in possible_moves_grid.items():
        if is_pellet_in_sight(pac_pos, pos) and possible_moves > best_move_value and pos not in last_known_pac_pos and pos not in pac_current_moves:
            best_move = pos
            best_move_value = possible_moves
    return best_move



get_grid()

#orig_grid = grid.copy()
possible_moves_grid = calculate_possible_moves(grid)

# game loop
while True:
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight

    my_pac = {}
    enemy_pac = {}
    my_pac_locations = [] 
    pac_current_moves = []

    for i in range(visible_pac_count):
        # pac_id: pac number (unique within a team)
        # mine: true if this pac is yours
        # x: position in the grid
        # y: position in the grid
        # type_id: unused in wood leagues
        # speed_turns_left: unused in wood leagues
        # ability_cooldown: unused in wood leagues
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        mine = mine != "0"
        x = int(x)
        y = int(y)
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)

        grid[(x, y)] = VISITED
        if mine:
            my_pac[pac_id] = { "pos" : (x, y), "type_id" : type_id, "speed_turns_left": speed_turns_left, "ability_cooldown" : ability_cooldown }
            my_pac_locations.append((x, y))
        else:
            enemy_pac[pac_id] = { "pos" : (x, y), "type_id" : type_id, "speed_turns_left": speed_turns_left, "ability_cooldown" : ability_cooldown }


    visible_pellet_count = int(input())  # all pellets in sight

    # for (key, value) in grid.items():
    #     if value >= 1:
    #         grid[key] = INVISIBLE_LOCATION
    
    pellet_locations = []
    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        x, y, value = [int(j) for j in input().split()]
        grid[(x, y)] = value
        pellet_locations.append((x, y))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # MOVE <pacId> <x> <y>
    command = ""
    for (key, value) in my_pac.items():
        pac_id = key
        pac_pos = value["pos"]
        my_type_id = value["type_id"]
        speed_turns_left = value["speed_turns_left"]
        ability_cooldown = value["ability_cooldown"]
        for y in range(height):
            possible_pellet = (pac_pos[0], y)
            if is_pellet_in_sight(pac_pos, possible_pellet, False) and possible_pellet not in pellet_locations:
                grid[possible_pellet] = VISITED
        for x in range(width):
            possible_pellet = (x, pac_pos[1])
            if is_pellet_in_sight(pac_pos, possible_pellet, False) and possible_pellet not in pellet_locations:
                grid[possible_pellet] = VISITED
        if len(enemy_pac) > 0 and ability_cooldown == 0:
            did_i_switch = False
            for enemy_value in enemy_pac.values():
                enemy_pac_pos = enemy_value["pos"]
                enemy_type_id = enemy_value["type_id"]
                enemy_distance = get_eucliadian_distance(pac_pos, enemy_pac_pos)
                if enemy_distance <= 2 and (collision_matrix[enemy_type_id] == my_type_id or collision_matrix[my_type_id] != enemy_type_id):
                    for winner, loser in collision_matrix.items():
                        if loser == enemy_type_id and not did_i_switch:
                            command += "SWITCH {} {} | ".format(pac_id, winner)
                            did_i_switch = True
            if did_i_switch:
                continue
        if ability_cooldown == 0:
            command += "SPEED {} | ".format(pac_id)
            continue
        new_pos, distance = get_closest_pellet(pac_pos)        
        if pac_pos == new_pos:
            new_pos = find_move(pac_pos, last_known_pos[pac_id][-1 * math.floor(diagonal_distance/4):])
        pac_current_moves.append(new_pos)
        grid[new_pos] = VISITED
        command += "MOVE {} {} {} | ".format(pac_id, new_pos[0], new_pos[1])
        last_known_pos[pac_id].append(pac_pos)
    print(command)




