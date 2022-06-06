from mapping import Location


class Player:

    """This class is used to instance the human and the gnome objects.
    
    Arguments:
    
    name -- A string representing the name of the object
    xy -- The x and y coordinates (integers) on the map which determine the Location of the object
    hit_points -- An integer value which represents the amount of damage the object can take before dying"""

    def __init__(self, name: str, xy: Location, hit_points: int):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        
    def hp(self, value):
        """Sets a new value for the attribute 'hp'
        
        Arguments:
        
        value -- The new value of the object's 'hp' attribute"""
        self.hp = value
        
    def loc(self):
        """Returns the current Location of the object on the map"""
        return self.x, self.y

    def move_to(self, xy):
        """Sets a new Location of the object on the map"""
        self.x, self.y = xy
            
    def die(self):
        """Sets the 'face' attribute of the object (which gets rendered onto the terminal)
        to a skull character, indicating the object (gnome or human) has died."""
        self.face = '☠'

    def get_hit_points(self):
        """Returns the current value of the object's 'hp' attribute"""
        return self.hp

    def __str__(self):
        """Returns the value of the object's 'hp' attribute"""
        return self.name

    def __repr__(self):
        """Retruns a string with the object's name, loc, and hp attributes"""
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"