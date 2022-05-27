class Player:
    def __init__(self, name, xy, hit_points=100):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        self.max_hp = hit_points

    #@hp.setter
    def hp(self, value):
        self.hp = value
        
    def loc(self):
        return self.x, self.y

    def move_to(self, xy):
        self.x, self.y = xy
    
    def kill(self):
        self.hp = 0
        self.alive = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"