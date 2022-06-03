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

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def set_sword(self):
       self.weapon = 'Sword'

    def set_picaxe(self):
        self.tool = 'Picaxe'

    def set_amulet(self):
        self.treasure = 'Amulet'