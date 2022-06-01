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


#def attack(dungeon, player, ...): # completar
    # completar
    raise NotImplementedError


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

    if num == 1:
        if right[0] < 80:
            return right
    
    elif num == 2:
        if up[1] > 0:
            return up
    
    elif num == 3:
        if left[0] > 0:
            return left
    
    elif num == 4:
        if down[1] < 80:
            return down
    
    else:
        return loc_gnome

def random_player_spawn():

    rows = random.randrange(1, 25)
    columns = random.randrange(1, 80)

    return columns, rows
    
def move(human, direction):
    loc_human = human.loc()
    new_locs = ((loc_human[0], loc_human[1] - 1), (loc_human[0], loc_human[1] + 1), (loc_human[0] - 1, loc_human[1]), (loc_human[0] + 1, loc_human[1]))

    if direction == "up":
        if loc_human[1] - 1 > -1:
            return new_locs[0]
    
    elif direction == "down":
        if loc_human[1] + 1 < 25:
            return new_locs[1]

    elif direction == "left":
        if loc_human[0] - 1 > 1:
            return new_locs[2]

    elif direction == "right":
        if loc_human[0] + 1 < 80:
            return new_locs[3]

    return loc_human

#CODIGO REPETIDO

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError