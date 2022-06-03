import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.hp = 50
        self.alive = True
        self.face = 'G'

    def gnome_receive_damage(self):
        self.hp -= int(random.random() * 20) + 5
        if self.hp < 0:
            self.hp = 0
    
    def get_hp(self):
        return self.hp