import random
from player import Player

class Gnome(Player):

    """This class models the gnome object. It inherits all of
    its attributes from the Player class (see player.py)
    
    Arguments:
    
    name -- A string representing the object's name
    xy -- The x and y coordinates of the object on the map"""

    def __init__(self, name: str, xy: tuple):
        super().__init__(name, xy, 100)
        self.hp = 100
        self.alive = True
        self.face = 'G'

    def gnome_receive_damage(self):
        """Decreases the gnome's hp by a 
        random integer betweeen 5 and 25 by changing the value
        of the 'hp' attribute"""
        self.hp -= int(random.random() * 20) + 5
        if self.hp < 0:
            self.hp = 0