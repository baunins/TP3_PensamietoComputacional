import random
from player import Player


class Human(Player):
    def __init__(self, name, xy, hit_points):
        super().__init__(name, xy, hit_points)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def has_sword(self):
        if self.weapon == None:
            return False
        elif self.weapon != None:
            return True

    def has_sword(self):
        if self.tool == None:
            return False
        elif self.tool != None:
            return True

human = Human("Felpa", (9, 10), 100)