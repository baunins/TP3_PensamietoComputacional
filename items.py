from typing import Union


numeric = Union[float, int]


class Item:
    def __init__(self, name, fc, type):
        self.name = name
        self.face = fc
        self.type = type

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', '{self.face}')"


class Sword(Item):
    def __init__(self, min_dmg: numeric, max_dmg: numeric):
        super().__init__('Sword', '⚔', 'weapon')
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg


class Amulet(Item):
    def __init__(self):
        super().__init__('Amulet', '💎', 'treasure')


class PickAxe(Item):
    def __init__(self):
        super().__init__('Pickaxe', "⛏️", 'tool')