import time
import mapping
#import magic
import msvcrt


from gnome import Gnome
from human import Human
from items import Amulet, PickAxe, Sword
import actions
from player import Player


ROWS = 25
COLUMNS = 80

def read_key(key, player, dungeon):

    dicc = {'w': 'up',
    's': 'down', 
    'a': 'left', 
    'd': 'right'}

    if key in dicc: 

        move_player = actions.move(player, dicc.get(key))
        print(player.tool)
        if player.tool == None:
            if dungeon.is_walkable(move_player) == True:
                player.move_to(move_player)
        elif player.tool == "Picaxe":
            dungeon.dig(move_player)
            player.move_to(move_player)

        move_gnome = actions.random_gnome_movement(gnome_object)
        if dungeon.is_walkable(move_gnome) == True:
            gnome_object.move_to(move_gnome)

    elif key not in dicc:
        player.loc()

            

if __name__ == "__main__":

    # initial parameters
    level = 0
    player_object = Human("Felpa", actions.random_player_spawn())
    gnome_object = Gnome('Gnome', actions.random_player_spawn())
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
        dungeon.new_level(player_object.loc())
        dungeon.render(player_object, gnome_object)

        print('Player Hit Points: ', player_object.get_hit_points())
        print('Gnome Hit Points: ', gnome_object.get_hit_points())

        if player_object.loc() == gnome_object.loc():
            gnome_object.gnome_hp_damage()

        # read key
        key = msvcrt.getch().decode('UTF-8')
        #key = magic.read_single_keypress()
        # Hacer algo con keys:
                
        if key[0] == 'w':

            read_key('w', player_object, dungeon)
                
        elif key[0] == 'a':

            read_key('a', player_object, dungeon)
            
        elif key[0] == 's':
            
            read_key('s', player_object, dungeon)

        elif key[0] == 'd':

            read_key('d', player_object, dungeon)

        elif key[0] == 'e':
            actions.pickup(dungeon, player_object)