import time
import mapping
import magic


from gnome import Gnome
from human import Human
from items import Item, Sword
import actions
from player import Player


ROWS = 25
COLUMNS = 80

def read_key(key):

    dicc = {'w': 'up',
    's': 'down', 
    'a': 'left', 
    'd': 'right'}

    if key in dicc: 

        move_player = actions.move(player, dicc.get(key))
        if dungeon.is_walkable(move_player) == True:
            player.move_to(move_player)

        move_gnome = actions.random_gnome_movement(gnome)
        while dungeon.is_walkable(move_gnome) == False:
            move_gnome = actions.random_gnome_movement(gnome)
        gnome.move_to(move_gnome)

    elif key not in dicc:
        player.loc()

            

if __name__ == "__main__":

    # initial parameters
    level = 0
    player = Human("Felpa", (10, 10), 100)
    gnome = Gnome('Gnome', (12, 7))
    #sword = Sword(20, 30, (15, 20))

    # initial locations may be random generated
    #gnomes =

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    #dungeon.add_item(sword)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    turns = 0
    while dungeon.level >= 0:
        turns += 1

        dungeon.render(player, gnome)
        # read key
        key = magic.read_single_keypress()
        # Hacer algo con keys:
                
        if key[0] == 'w':

            read_key('w')
                
        elif key[0] == 'a':

            read_key('a')
            
        elif key[0] == 's':
            
            read_key('s')

        elif key[0] == 'd':

            read_key('d')


        # move player and/or gnomes

    #if player has amulet:
        #win!
    #elif player doesn't have amulet:
        #lose :(
    # Salió del loop principal, termina el juego