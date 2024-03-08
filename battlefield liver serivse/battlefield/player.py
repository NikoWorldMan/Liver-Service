
#
# player.py
# player class
#
import time
import random
import effects
import entity
import item as items

from entity import Stats

class Player(entity.Entity):   
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg, inv_space, weapon_space, currency, xp ,xpmax):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)

        self.biome = None

        self.stats[Stats.MANA] = mana
        self.set_stats()
        self.mana = self.stat[Stats.MANA]

        self.xp = xp
        self.xpmax = xpmax

        self.inv = []

        self.inv_space = inv_space
        self.weapon_space = weapon_space
        self.currency = currency

    def level_up(self, rolls):
        print("you leveled up!")

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xpmax:
            self.xp -= self.xpmax
            self.xpmax += self.xpmax/10 + 40

            self.level_up(5)





    def action_loop(self):
        print()
        print(f'Select one of the following actions:\nShop: (S) | Fight: (F) | Dungeon: (D) | Inventory: (I) | Armory: (A) ')
        user_input = input('What would you like to do now? ').lower()

        if user_input == 'i':

            num = 0
            count = []
            for item in self.inv:

                if item.type == items.ItemTypes.ITEM:
                    num += 1
                    count.append(str(num))




        elif user_input == 'f':
            print("fight")

        elif user_input == 's':
            print("shop")

        elif user_input == 'a':
            print("armory")

        elif user_input == 'd':
            print("dungeon")


    def combat_loop(self, team):

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

    def collect_item(self, inv, item):
        
        if item in inv:
            index = inv.index(item)
            inv[index].count += item.count
        else:
            inv.append(item)

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

class Mage(Magic):
    type = 'Mage'
    desc = "Has access to powerful spells, but has slow speed"
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg)
class Necromancer(Magic):
    type = 'Necromancer'
    desc = "Summons minions to aid in battles"
    def __init__(self, name, level, health, mana, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg)
        
class Hunter(Player):
    desc = "Can deal high single target damage, and has high speed"
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)
class Warrior(Player):
    desc = "High survivalility class with AoE attacks"
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)    

