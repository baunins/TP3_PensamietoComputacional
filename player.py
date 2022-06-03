class Player:
    def __init__(self, name, xy, hit_points):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        
    def hp(self, value):
        self.hp = value
        
    def loc(self):
        return self.x, self.y

    def move_to(self, xy):
        self.x, self.y = xy
            
    def die(self):
        self.face = '💀'

    def get_hit_points(self):
        return self.hp

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"