#
#
#

from battlefield.entity import Stats
import copy


class ItemTypes:
    CONSUMABLE = 'Consumable'
    ITEM = 'Item'
    COMBAT = 'Combat'

class Items:
    def __init__(self, name, count, type: ItemTypes, price) -> None:

        self.price = price
        self.name: str = name
        self.count: int = count
        self.type: ItemTypes = type

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        return f'{self.name}' if self.count <= 1 else f'{self.name} (x{self.count})'
    
    def use_attempt(self, user, inv):
        self.use_item(user, inv) if self in inv else None

    def use_item(self, user, inv):
        if self in inv:
            user.set_stats()

            self.count -=1
            if self.count < 1:
                inv.remove(self)
        else:
            return False
        user.set_stats()

class HealthPotion(Items):
    def __init__(self, name, count, heal_amount, maxhealth_mult, type: ItemTypes, price) -> None:
        super().__init__(name, count, type, price)

        self.healing = heal_amount
        self.maxhealth_mult = maxhealth_mult

    def use_item(self, user, inv):
        super().use(user, inv)
        
        heal = self.healing + self.maxhealth_mult * user.stat[Stats.HEALTH]
        user.change_health(heal)
        print(f"{user.name} used {self.name} and healed {heal} health!")
"""
the_item = HealthPotion("Great omegus healus", 1, 1000, 0.4, [ItemTypes.CONSUMABLE] )

print(the_item.display())
print(the_item.type)
"""
