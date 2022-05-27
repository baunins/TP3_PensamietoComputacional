import time
import mapping
import magic

import random
from gnome import Gnome
from human import Human
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
        # render map
        dungeon.render(player)

        # read key
        key = magic.read_single_keypress()
        # Hacer algo con keys:

        if key[-1] == 'w':
            actions.move_up(mapping.dungeon, player, gnome)

        elif key[-1] == 'a':
            actions.move_left(mapping.dungeon, player, gnome)
        
        elif key[-1] == 's':
            actions.move_down(mapping.dungeon, player, gnome)

        elif key[-1] == 'd':
            actions.move_right(mapping.dungeon, player, gnome)

        # move player and/or gnomes

    #if player has amulet:
        #win!
    #elif player doesn't have amulet:
        #lose :(
    # Salió del loop principal, termina el juego