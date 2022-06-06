from typing import Union

import mapping
import random
import player
import human
import gnome

numeric = Union[int, float]

def random_spawn():

    """Returns a random location on the map.
    Some rows and columns were excluded to avoid a RecursionError in the future."""

    rows = random.randrange(3, 22)
    columns = random.randrange(15, 70)

    return columns, rows


def random_gnome_movement(gnome: gnome.Gnome):

    """Returns a random walkable Location for the gnome to move to.
    
    Arguments:
    
    gnome -- an instance of the Gnome class (see gnome.py)"""

    loc_gnome = gnome.loc()

    right = (loc_gnome[0] + 1, loc_gnome[1])
    up = (loc_gnome[0], loc_gnome[1] - 1)
    left = (loc_gnome[0] - 1, loc_gnome[1])
    down = (loc_gnome[0], loc_gnome[1] + 1)
    
    num = random.randrange(1, 5)
    
    if gnome.get_hit_points() != 0:
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

def player_picaxe_spawn(dungeon: mapping.Dungeon):

    """Returns the spawn Locations of the human and picaxe on the map
    in order for them to be connected by walkable tiles.
    
    Arguments:
    
    dungeon -- An instance of the class Dungeon (see mapping.py)"""
    
    player_loc = random_spawn()
    picaxe_loc = random_spawn()

    try:
        if dungeon.are_connected(player_loc, picaxe_loc) == True:
            dungeon.checked = []
            return player_loc, picaxe_loc
        dungeon.checked = []
        return player_picaxe_spawn(dungeon)
    
    except RecursionError:
        print("The game wasn't able to launch properly. Please kill the terminal and re-run the program.")
        return player_picaxe_spawn(dungeon)

def gnome_spawn(dungeon: mapping.Dungeon):


    """Returns the spawn Location of the gnome on the map
    in order for it to be connected by walkable tiles to the human.
    
    Arguments:
    
    dungeon -- An instance of the class Dungeon (see mapping.py)"""


    player_loc = random_spawn()
    gnome_loc = random_spawn()
    
    try:
        if dungeon.are_connected(player_loc, gnome_loc) == True:
            dungeon.checked = []
            return gnome_loc
        dungeon.checked = []
        return gnome_spawn(dungeon)
    
    except RecursionError as e:
        print("The game wasn't able to launch properly. Please kill the terminal and re-run the program.")
        return gnome_spawn(dungeon)
        
    
def move(human: human.Human, direction: str):

    """Returns a new Location on the map for the human depending
    on the given direction
    
    Arguments:

    human - 
    
    direction -- A string which indicates what the new Location for the human should be."""

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


def pickup(dungeon: mapping.Dungeon, human: human.Human):

    """Picks an item and assings it to the human object.
    
    Arguments:
    
    dungeon -- An instance of the Dungeon class.
    
    human -- An instance of the Human class."""

    item = str(dungeon.get_items(human.loc()))

    if len(item) > 0:
        if item == "[Item('Sword', '⚔')]":
            human.set_sword()

        elif item == "[Item('Pickaxe', '⛏️')]":
            human.set_picaxe()

        elif item == "[Item('Amulet', '♢')]":
            human.set_amulet()

        elif item == "[Item('Apple', '*')]":
            human.heal(30)