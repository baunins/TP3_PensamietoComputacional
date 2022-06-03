import random
from player import Player


class Human(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 100)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'
        self.hp = 100

    def set_sword(self):
       self.weapon = 'Sword'

    def set_picaxe(self):
        self.tool = 'Picaxe'

    def set_amulet(self):
        self.treasure = 'Amulet'

    def has_amulet(self):
        if self.treasure == 'Amulet':
            return True
        return False

    def has_sword(self):
        if self.weapon == 'Sword':
            return True
        return False
    
    def human_receive_damage(self):
        self.hp -= int(random.random() * 20)
        if self.hp < 0:
            self.hp = 0

    def get_tools(self):
        if self.tool == 'Picaxe':
            return 'Picaxe'
        return 'No tools'

    def get_weapons(self):
        if self.weapon == 'Sword':
            return 'Sword'
        return 'No weapons'
    
    def get_amulet(self):
        if self.treasure == 'Amulet':
            return 'Grabbed!'
        return 'No Amulet'