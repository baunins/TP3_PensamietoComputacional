from typing import Union, Tuple

from game import ROWS, COLUMNS
import mapping
import random
import player
from human import human
from gnome import gnome


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

    rows = random.randrange(1, ROWS)
    columns = random.randrange(1, COLUMNS)

    return rows, columns

def random_gnome_movement():

    loc_gnome = gnome.loc()
    
    num = random.randrange(1, 5)

    if num == 1:
        return (loc_gnome[0], loc_gnome[1] + 1)
    
    elif num == 2:
        return (loc_gnome[0] - 1, loc_gnome[1])
    
    elif num == 1:
        return (loc_gnome[0], loc_gnome[1] - 1)
    
    elif num == 1:
        return (loc_gnome[0] + 1, loc_gnome[1])
    

def move_up(dungeon: mapping.Dungeon, human, gnome):
    
    loc_human = human.loc()
    new_loc_human = (loc_human[0], loc_human[1] + 1)
    new_loc_gnome = random_gnome_movement()

    human.move_to(new_loc_human)
    gnome.move_to(new_loc_gnome)


def move_down(dungeon: mapping.Dungeon, human, gnome):
    
    loc_human = human.loc()
    new_loc_human = (loc_human[0], loc_human[1] - 1)
    new_loc_gnome = random_gnome_movement()

    human.move_to(new_loc_human)
    gnome.move_to(new_loc_gnome)


def move_left(dungeon: mapping.Dungeon, human, gnome):
   
    loc_human = human.loc()
    new_loc_human = (loc_human[0] - 1, loc_human[1])
    new_loc_gnome = random_gnome_movement()

    human.move_to(new_loc_human)
    gnome.move_to(new_loc_gnome)


def move_right(dungeon: mapping.Dungeon, human, gnome):
    
    loc_human = human.loc()
    new_loc_human = (loc_human[0] + 1, loc_human[1])
    new_loc_gnome = random_gnome_movement()

    human.move_to(new_loc_human)
    gnome.move_to(new_loc_gnome)


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError