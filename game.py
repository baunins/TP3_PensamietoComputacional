
import mapping
import magic


from gnome import Gnome
from human import Human
from items import Amulet, PickAxe, Sword, Food
import actions
from player import Player
import sys

sys.setrecursionlimit(20000)


ROWS = 25
COLUMNS = 80

def read_key(key, player, dungeon, gnome):

    """Given the letters, 'w', 'a', 's' and 'd', moves the human
    upwards, to the left, downwards, and to the right, respectively.
    Then, it randomly moves the gnome.
    
    Arugments:
    
    key -- A string containing a single letter
    
    player -- An instance of the Human class
    
    dungeon -- An instance of the class Dungeon
    
    gnome -- An instance of the class Gnome"""

    dicc = {'w': 'up',
    's': 'down', 
    'a': 'left', 
    'd': 'right'}

    if key in dicc: 

        move_player = actions.move(player, dicc.get(key))
        if player.tool == None:
            if dungeon.is_walkable(move_player) == True:
                player.move_to(move_player)
        elif player.tool == "Picaxe":
            dungeon.dig(move_player)
            player.move_to(move_player)

        move_gnome = actions.random_gnome_movement(gnome)
        if dungeon.is_walkable(move_gnome) == True:
            gnome.move_to(move_gnome)

    elif key not in dicc:
        player.loc()

def main():

    """Runs the entire game"""

    name = input("\nWelcome to the dungeons! What's your name?\n\n> ")
    input(f'''\n\nGreat, {name}! Your objective is to grab the amulet "♢", hidden in the lowest dungeon,
and escape with it.\n\nBut beware! The gnome "G" will kill you if you're not careful.
\nThe picaxe "⛏️" can help you destroy walls in the dungeons and the sword "⚔" can help you kill the gnome.
You can eat the apple "*" to recover hitpoints if you're hurt.
Whenever you're ready, press enter to start the game!\n\nGood luck out there, {name}!''')

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    player = Human("Felpa", actions.player_picaxe_spawn(dungeon)[0])
    gnome = Gnome('Gnome', actions.gnome_spawn(dungeon))
    item_sword = Sword()
    item_amulet = Amulet()
    item_pickaxe = PickAxe()
    item_food = Food()

    dungeon.add_item(item_sword, 1, actions.random_spawn())
    dungeon.add_item(item_amulet, 3, actions.random_spawn())
    dungeon.add_item(item_pickaxe, 1, actions.player_picaxe_spawn(dungeon)[1])
    dungeon.add_item(item_food, 1, actions.random_spawn())

    turns = 0
    while dungeon.level >= 0:
        turns += 1
        dungeon.new_level(player.loc())
        dungeon.render(player, gnome)

        print(f"{name}'s HP: {player.get_hit_points()} | Gnome's HP: {gnome.get_hit_points()} | Tools: {player.get_tools()} | Weapons: {player.get_weapons()} | Amulet: {player.get_amulet()}")      

        if player.loc() in [gnome.loc(), (gnome.loc()[0]+1, gnome.loc()[1]), (gnome.loc()[0]-1, gnome.loc()[1]),
        (gnome.loc()[0], gnome.loc()[1]+1), (gnome.loc()[0], gnome.loc()[1]-1), (gnome.loc()[0]+1, gnome.loc()[1]+1),
        (gnome.loc()[0]-1, gnome.loc()[1]-1), (gnome.loc()[0]+1, gnome.loc()[1]-1), (gnome.loc()[0]-1, gnome.loc()[1]+1)]:
            if player.has_sword() == True:
                gnome.gnome_receive_damage()
            if gnome.get_hit_points() != 0:
                player.human_receive_damage()
        
        if gnome.hp == 0:
            gnome.die()
            dungeon.render(player, gnome)
        
        if player.hp == 0:
            player.die()
            dungeon.render(player, gnome)
            print("You died!")
            exit()

        key = magic.read_single_keypress()
                
        if key[0] == 'w':

            read_key('w', player, dungeon, gnome)
                
        elif key[0] == 'a':

            read_key('a', player, dungeon, gnome)
            
        elif key[0] == 's':
            
            read_key('s', player, dungeon, gnome)

        elif key[0] == 'd':

            read_key('d', player, dungeon, gnome)

        elif key[0] == 'e':
            actions.pickup(dungeon, player)
        
    if dungeon.level == -1 and player.has_amulet() == True:
        print(f'Congratulations, {name}! You succesfully escaped with the amulet!')
        exit()
    elif dungeon.level == -1 and player.has_amulet() == False:
        print(f'Game over. {name} escaped the dungeons without the amulet.')
        exit()

if __name__ == "__main__":

    main()