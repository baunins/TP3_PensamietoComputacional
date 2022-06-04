from typing import Union, Tuple

import mapping
import random
import player

numeric = Union[int, float]

def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def move_to(dungeon: mapping.Dungeon, player: player.Player, location: Tuple[numeric, numeric]):
    # completar
    raise NotImplementedError

def random_gnome_movement(gnome):

    loc_gnome = gnome.loc()

    right = (loc_gnome[0] + 1, loc_gnome[1])
    up = (loc_gnome[0], loc_gnome[1] - 1)
    left = (loc_gnome[0] - 1, loc_gnome[1])
    down = (loc_gnome[0], loc_gnome[1] + 1)
    
    num = random.randrange(1, 5)
    
    if gnome.get_hp() != 0:
        if num == 1:
            if right[0] < 80:
                return right
        
        elif num == 2:
            if up[1] > -1:
                return up
        
        elif num == 3:
            if left[0] > 0:
                return left
        
        elif num == 4:
            if down[1] < 25:
                return down
    
    return loc_gnome

def player_picaxe_spawn(dungeon):
    
    player_loc = random_spawn()
    picaxe_loc = random_spawn()

    try:
        if dungeon.are_connected(player_loc, picaxe_loc) == True:
            dungeon.checked = []
            return player_loc, picaxe_loc
        dungeon.checked = []
        return player_picaxe_spawn(dungeon)
    
    except RecursionError as e:
        return player_picaxe_spawn(dungeon)

def gnome_spawn(dungeon):

    player_loc = random_spawn()
    gnome_loc = random_spawn()
    
    try:
        if dungeon.are_connected(player_loc, gnome_loc) == True:
            dungeon.checked = []
            return gnome_loc
        dungeon.checked = []
        return gnome_spawn(dungeon)
    
    except RecursionError as e:
        return gnome_spawn(dungeon)
        
        

def random_spawn():

    rows = random.randrange(3, 22)
    columns = random.randrange(10, 71)

    return columns, rows
    
def move(human, direction):

    loc_human = human.loc()
    new_locs = ((loc_human[0], loc_human[1] - 1), (loc_human[0], loc_human[1] + 1), 
    (loc_human[0] - 1, loc_human[1]), (loc_human[0] + 1, loc_human[1]))

    if direction == "up":
         if loc_human[1] - 1 > -1:
             return new_locs[0]
   
    elif direction == "down":
         if loc_human[1] + 1 < 25:
             return new_locs[1]

    elif direction == "left":
         if loc_human[0] - 1 > -1:
             return new_locs[2]

    elif direction == "right":
         if loc_human[0] + 1 < 80:
             return new_locs[3]

    return loc_human



def climb_stair(dungeon: mapping.Dungeon, player: player.Player, level):
    
    level -=1


def descend_stair(dungeon: mapping.Dungeon, player: player.Player, level):
    
    level += 1

def pickup(dungeon: mapping.Dungeon, human: player.Player):

    item = str(dungeon.get_items(human.loc()))

    if len(item) > 0:
        if item == "[Item('Sword', '⚔')]":
            human.set_sword()

        elif item == "[Item('Pickaxe', '⛏️')]":
            human.set_picaxe()

        elif item == """[Item('Amulet', '♢')]""":
            human.set_amulet()

            