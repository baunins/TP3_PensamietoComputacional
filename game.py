import time
import mapping
import magic

from gnome import Gnome
from human import Human, human
from items import Item
import actions
from player import Player


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":

    # initial parameters
    level = 0
    player = Human("Felpa", actions.random_player_spawn(), 100)
    gnome = gnome = Gnome('Gnome', (12, 7))

    # initial locations may be random generated
    #gnomes =

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    turns = 0
    while dungeon.level >= 0:
        turns += 1

        dungeon.render(human, gnome)

        # read key
        key = magic.read_single_keypress()
        # Hacer algo con keys:

        if key[-1] == 'w':
            move = actions.move_up(dungeon, human)
            move_player = move[0]
            move_gnome = move[1]

            if dungeon.is_walkable(move_player) == True:
                human.move_to(move_player)

            if dungeon.is_walkable(move_gnome) == True:
                gnome.move_to(move_gnome)

        elif key[-1] == 'a':

            move = actions.move_left(dungeon, human)
            move_player = move[0]
            move_gnome = move[1]

            if dungeon.is_walkable(move_player) == True:
                human.move_to(move_player)

            if dungeon.is_walkable(move_gnome) == True:
                gnome.move_to(move_gnome)
        
        elif key[-1] == 's':
        
            move = actions.move_down(dungeon, human)
            move_player = move[0]
            move_gnome = move[1]

            if dungeon.is_walkable(move_player) == True:
                human.move_to(move_player)

            if dungeon.is_walkable(move_gnome) == True:
                gnome.move_to(move_gnome)

        elif key[-1] == 'd':

            move = actions.move_right(dungeon, human)
            move_player = move[0]
            move_gnome = move[1]

            if dungeon.is_walkable(move_player) == True:
                human.move_to(move_player)

            if dungeon.is_walkable(move_gnome) == True:
                gnome.move_to(move_gnome)


        # move player and/or gnomes

    #if player has amulet:
        #win!
    #elif player doesn't have amulet:
        #lose :(
    # Salió del loop principal, termina el juego