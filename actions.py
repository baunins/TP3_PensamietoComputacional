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

def random_player_spawn():

    rows = random.randrange(1, 25)
    columns = random.randrange(1, 80)

    return rows, columns

def random_gnome_movement(gnome):

    loc_gnome = gnome.loc()
    
    num = random.randrange(1, 5)

    if num == 1:
        return (loc_gnome[0], loc_gnome[1] + 1)
    
    elif num == 2:
        return (loc_gnome[0] - 1, loc_gnome[1])
    
    elif num == 3:
        return (loc_gnome[0], loc_gnome[1] - 1)
    
    elif num == 4:
        return (loc_gnome[0] + 1, loc_gnome[1])
    
def move(human, direction):
    loc_human = human.loc()
    new_locs = ((loc_human[0], loc_human[1] - 1), (loc_human[0], loc_human[1] + 1), (loc_human[0] - 1, loc_human[0]), (loc_human[0] + 1, loc_human[0]))


    if loc_human[1] - 1 > 1 and loc_human[1] + 1 < 25 and loc_human[0] - 1 > 1 and loc_human[0] + 1 < 80:
        if direction == "up":
            return new_locs[0]
        elif direction == "down":
            return new_locs[1]
        elif direction == "left":
            return new_locs[2]
        elif direction == "right":
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