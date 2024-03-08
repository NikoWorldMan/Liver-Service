#
#
#
#

from entity import Entity
from entity import Stats
import random

class mob(Entity):
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)
        self.loot = []

    def attack_options(self, team):
        return super().attack_options(team)



class Creeper(mob):
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg, fuse):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)
        self.stats[Stats.FUSE] = fuse

    def attack_options(self, team):
        self.stats[Stats.FUSE] -=1

        if self.stats[Stats.FUSE] > 0:
            print(self.name,"Will explode in",self.stats[Stats.FUSE],"Turns!\n")
            self.attack(random.choice(team), 0.75, 0)
        else:
            print(self.name,"Exploded!")
            for entity in team:
                self.attack(entity, 2, 0)

class Zombie(mob):
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)

    def attack_options(self, team):
        
        if random.randrange(0,2) > 0:
            self.attack(random.choice(team), 1.5, 0)
        else:
            self.attack(random.choice(team), 1.5, 0)

class Wizard(mob):
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)

    def attack_options(self, team):

            self.attack(random.choice(team), 1, 0),