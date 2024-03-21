#
#
#

from battlefield.entity import Stats
from battlefield.effects import Effects
import copy


class ItemTypes:
    CONSUMABLE = 'Consumable'
    ITEM = 'Item'
    COMBAT = 'Combat'
    WEAPON = 'Weapon'

class Items:
    def __init__(self, name, count, price, storage, type: ItemTypes) -> None:

        self.storage = storage
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
    def __init__(self, name, count, heal_amount, maxhealth_mult, price, storage) -> None:
        super().__init__(name, count, price, storage, ItemTypes.CONSUMABLE)

        self.healing = heal_amount
        self.maxhealth_mult = maxhealth_mult

    def use_item(self, user, inv) -> list[str]:
        super().use_item(user, inv)
        
        heal = self.healing + self.maxhealth_mult * user.stat[Stats.HEALTH].stat
        user.change_health(heal)

        return [f"{user.name} used '{self.name}' and healed {int(heal)} health!"]

class Key(Items):
    def __init__(self, name, count, price, storage) -> None:
        super().__init__(name, count, price, storage, ItemTypes.ITEM)

class ManaPotion(Items):
    def __init__(self, name, count, restore_amount: int, maxmana_mult: int, price, storage) -> None:
        super().__init__(name, count, price, storage, ItemTypes.CONSUMABLE)

        self.amount = restore_amount
        self.mult = maxmana_mult

    def use_item(self, user, inv):
        if Stats.MANA in user.stat:
            super().use_item(user, inv)

            amount = self.amount + self.mult * user.stat[Stats.MANA].stat

            return [f"{user.name} used '{self.name}' and restored {int(amount)} mana!"]
        else:
            return [f"{self.name} cannot be used, user does not use mana!"]

class EffectPotion(Items):
    def __init__(self, name: str, count: int, price: int, storage: int, effects: list[Effects], duration: int) -> None:
        super().__init__(name, count, price, storage, ItemTypes.COMBAT)

        self.duration = duration
        self.effects = effects

class RandomBox(Items):
    def __init__(self, name: str, count: int, price: int, storage: int, rolls: int, item_pool: list | None) -> None:
        super().__init__(name, count, price, storage, ItemTypes.CONSUMABLE)

        self.rolls = rolls
        self.items = item_pool

    def use_item(self, user, inv):
        return super().use_item(user, inv)
"""
the_item = HealthPotion("Great omegus healus", 1, 1000, 0.4, [ItemTypes.CONSUMABLE] )

print(the_item.display())
print(the_item.type)
"""
