import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.hp = 50
        self.alive = True
        self.face = 'G'

    def damage(self):
        return random.random() * 20

    def gnome_hp_damage(self):
        self.hp -= 10