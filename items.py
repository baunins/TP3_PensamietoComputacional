from typing import Union


numeric = Union[float, int]


class Item:
    """This class models any item object in the game.
    
    Arguments:
    
    name -- A string representing the item's name

    fc -- A string with a character which will be printed onto
    the terminal when the item spawns

    type -- The item's role within the game
    """
    def __init__(self, name: str, fc: str, type: str):
        self.name = name
        self.face = fc
        self.type = type

    def __str__(self):
        """Returns the value of the object's 'name' attribute"""
        return self.name

    def __repr__(self):
        """Returns a string containing the item's 'name' and 'face' attributes"""
        return f"Item('{self.name}', '{self.face}')"


class Sword(Item):
    """This class models the game's sword. It inherits all of the
    attributes of the Item class.
    """
    def __init__(self):
        super().__init__('Sword', '⚔', 'weapon')


class Amulet(Item):
    """This class models the game's amulet. It inherits all of the
    attributes of the Item class.
    """
    def __init__(self):
        super().__init__('Amulet', '♢', 'treasure')


class PickAxe(Item):
    """This class models the game's Picaxe. It inherits all of the
    attributes of the Item class.
    """
    def __init__(self):
        super().__init__('Pickaxe', "⛏️", 'tool')

class Food(Item):
    """This class models the game's apple. It inherits all of the
    attributes of the Item class.
    """
    def __init__(self):
        super().__init__('Apple', "*", 'food')