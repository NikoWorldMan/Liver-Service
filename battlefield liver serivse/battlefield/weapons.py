#
#
#
from battlefield.item import ItemTypes

class Weapon:
    def __init__(self, type: ItemTypes) -> None:
        self.type = type

    def abilities(self):
        ...