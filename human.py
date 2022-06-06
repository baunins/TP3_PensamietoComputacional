import random
from player import Player


class Human(Player):

    """The human is the object that the user plays as.
    This class inherits all of the attributes from the Player class (see player.py)
    
    Arguments:
    
    name -- The name of the human object
    
    xy -- The x and y coordinates of the object on the map
    """
    def __init__(self, name: str, xy: tuple[int, int]):
        super().__init__(name, xy, 100)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'
        self.hp = 100

    def set_sword(self):
        """Assings the 'Sword' item to the human as an attribute"""
        self.weapon = 'Sword'

    def set_picaxe(self):
        """Assings the 'Picaxe' item to the human as an attribute"""
        self.tool = 'Picaxe'

    def set_amulet(self):
        """Assigns the 'Amulet' item to the human as an attribute"""
        self.treasure = 'Amulet'

    def has_amulet(self):
        """Returns True if the human has the amulet or False if it doesn't"""
        if self.treasure == 'Amulet':
            return True
        return False

    def has_sword(self):
        """Retruns True if the human has the sword or False if it doesn't"""
        if self.weapon == 'Sword':
            return True
        return False
    
    def human_receive_damage(self):
        """Decreases the human's hp by a random integer between 0 and 20"""
        self.hp -= int(random.random() * 20)
        if self.hp < 0:
            self.hp = 0

    def get_tools(self):
        """Returns the string 'Picaxe' if the human has the picaxe or
        the string 'No tools' if it doesn't."""
        if self.tool == 'Picaxe':
            return 'Picaxe'
        return 'No tools'

    def get_weapons(self):
        """Returns the string 'Sword' if the human has the picaxe or
        the string 'No weapons if it doesn't."""
        if self.weapon == 'Sword':
            return 'Sword'
        return 'No weapons'
    
    def get_amulet(self):
        """Returns the string 'Amulet' if the human has the picaxe or
        the string 'No Amulet' if it doesn't."""
        if self.treasure == 'Amulet':
            return 'Grabbed!'
        return 'No Amulet'

    def heal(self, healing: int):
        """Increases the human's hit-points by a given amount.
        
        Arguments:
        
        healing -- An integer value by which the human's hp increases.
        """
        if self.hp > 99 - healing:
            self.hp = 100
        elif self.hp < 100 - healing:
            self.hp = self.hp + healing