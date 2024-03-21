#
#
#
#

import battlefield.effects
from battlefield.entity import Entity
from battlefield.entity import Stats
from battlefield.entity import Stat
import random

class mob(Entity):
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)
        self.maxlv = 100
        self.loot = []


    def attack_options(self, team):
        return super().attack_options(team)



class Example(mob):
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg): 
        # The different variables for the mob's stats
        
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg) 
        #Returns the stats, Any special stats need to be defined separately like so:
        #
        #self.fuse = fuse
        #
        #To add scaling based on level:
        #self.stat[Stats.FUSE] = fuse

        # Should look simular to this:
        #def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg, fuse):
        #   super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)
        #   self.stat[Stats.FUSE] = fuse


    def attack_options(self, team):
    #

        target = random.choice(team)
        #



