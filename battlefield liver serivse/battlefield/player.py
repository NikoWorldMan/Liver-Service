
#
# player.py
# player class
#
import time
import random
#import effects



import battlefield.entity as entity
import battlefield.item as items
import battlefield.weapons as weapons
from battlefield.item import ItemTypes
from battlefield.entity import Stats





class Player(entity.Entity):   
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg, item_space, weapon_space, currency, xp ,xpmax):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)

        self.states = []
        self.using_skill = None
        self.weapon = None

        self.maxlv = 80
        self.biome = None

        self.stats[Stats.MANA] = mana
        self.set_stats()
        self.mana = self.stat[Stats.MANA]

        self.xp: float = xp
        self.xpmax: float = xpmax

        self.inv: list = []

        self.item_space = item_space
        self.weapon_space = weapon_space
        self.currency = currency

    def level_up(self, rolls):
        print("you leveled up!")

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xpmax:
            self.xp -= self.xpmax
            self.xpmax += self.xpmax/10 + 5

            self.level_up(5)

    def get_inventory_space(self, type: list) -> int:
        space: int = 0
        for i in self.inv:
            if i.type in type:
                space += i.storage*i.count
        return space
    def get_total_inventory_space(self) -> int:
        space: int = 0
        for i in self.inv:
            space += i.storage*i.count
        return space


    def action_loop(self):
        print()
        print(f'Select one of the following actions:\nShop: (S) | Fight: (F) | Dungeon: (D) | Inventory: (I) | Armory: (A) ')
        user_input = input('What would you like to do now? ').lower()

        if user_input == 'i':


            for types in items.ItemTypes:
                num = 0
                count = []
                print(f'\n{types}:')

                for item in self.inv:
                    if item.type == items.ItemTypes.ITEM:
                        count += 1
                        num.append(str(count))

                    if item.type == items.ItemTypes.CONSUMABLE:
                        count += 1
                        num.append(str(count))

            print(f'')
            user_input = input(f'What item would you like to use?\n\n= ')

            if str(user_input) in num:
                num[user_input].use_item(self, self.inv)



        elif user_input == 'f':
            print("fight")

        elif user_input == 's':
            print("shop")

        elif user_input == 'a':
            print("armory")

        elif user_input == 'd':
            print("dungeon")

    def attack_options(self, team):

        userInput = ""
        while userInput!="f":

            for entity in team:
                entity.display_health()

            print()
            print("You have",self.health,"/",self.stat[Stats.HEALTH],"health")
            userInput=input("What do you do?\nInventory: (I) | Attack: (F) | Combat Items: (V) | Retreat: (X) ").lower()
            print(">^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<\n")

            if userInput == "i":

                print("- Items")
                displayInv(p, p.inventory, 0)
                print("\n- Consumable Items")
                displayInv(self.consumable_inv, 1)

            elif userInput =="f":
                print("Who do you want to attack? Cancel (e)")
                mob =random.choice(team)

                for entity in team:
                    entity.display_health()

                input()

                self.attack(mob, 1, 0)
                time.sleep(0.4)

                if mob.alive() == False:
                    print(f"Lv. {mob.level} {mob.name} died.")
                    team.remove(mob)

            elif userInput =="V":
                print("\n- Combat Items")
                displayInv(self.weapon_inv, 1)

            elif userInput =="x":
                print("\nYou got hurt while running away")
                self.health = 1
                print("you are now at",self.health,"health\n")
                return
    
    def list_inventory(self, inv, can_use):
        count = 0
        for item in inv:
            count +=1
            print(f"({count}) {item.display()}")

    def collect_item(self, item):

        for i in self.inv:
            if i.name == item.name:
                i.count += item.count
                return

        self.inv.append(item.clone())

    def initiate_battle(self, allies, opponents):
        pass

    def shop(self, shop):
        pass

    def options_loop(self):
        while True:
            pass
            
            userInput =""
            print("\nselect one of the following actions:\nShop: (S) | Fight: (F) | Dungeon: (D) | Inventory: (I) | Stats: (T) | Exit: (X)")   #
            userInput=input("what do you want to do now? ").lower()

            print("\n[ -------------------- ]\n")

            if userInput == "s":
                pass


class Magic(Player):
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)

        self.stats[Stats.MANA] = mana

class Templar(Player):
    type = 'Templar'
    desc = 'Posesses powerful attacks and shielding abilities'
    ability_info = 'Notable skills:\n- All attacks ignore some DEF and delays the enemy'
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg)

class Necromancer(Magic):
    type = 'Necromancer'
    desc = "Summons minions to aid in battles"
    ability_info = 'Notable skills:, Can summon monsters half i\'ts level'
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg)

class Psion(Player):
    type = 'Psion'
    desc = 'Has the power of mind control'
    ability_info = 'Notable skills: High speed, Life steal, Can make decoys of itself'
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg)

class Blightbringer(Magic):
    type = 'Malison Mage'
    desc = "Access to powerful spells, but has low speed"
    ability_info = 'Notable skills: Apply debuffs to enemies'
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg)

    def create_weapon(self, rarity: int, name: str | None):
        """
        rarity = 1 / 2 / 3
        Choosing any other number will cause the weapon to be of random rarity
        """

        
        if name is None:
            ...

        weapon = weapons.Weapon(ItemTypes.WEAPON)








classes = [Blightbringer, Necromancer, Psion, Templar]