import time
import mapping
import msvcrt


from gnome import Gnome
from human import Human
from items import Amulet, Item, PickAxe, Sword
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
    player = Human("Felpa", actions.random_player_spawn(), 100)
    gnome = Gnome('Gnome', actions.random_player_spawn())
    item_sword = Sword(20, 30) #falta pasarle el level
    item_amulet = Amulet() #falta pasarle el level
    item_pickaxe = PickAxe() #falta pasarle el level

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    dungeon.add_item(item_sword, 1, (20, 15))
    dungeon.add_item(item_amulet, 1, (13, 30))
    dungeon.add_item(item_pickaxe, 1)

    turns = 0
    while dungeon.level >= 0:
        turns += 1

        dungeon.render(player, gnome)
        # read key
        key = msvcrt.getch().decode('UTF-8')
        # Hacer algo con keys:
                
        if key[0] == 'w':

            read_key('w')
                
        elif key[0] == 'a':

            read_key('a')
            
        elif key[0] == 's':
            
            read_key('s')

        elif key[0] == 'd':

            read_key('d')