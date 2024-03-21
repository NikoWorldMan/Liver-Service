#
#
#
#

import battlefield.effects
from battlefield.mobs import mob
from battlefield.entity import Stats
import random



class Example(mob):
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg): 
        # The different variables for the mob's stats
        
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg) 
        #Returns the stats, Any special stats need to be defined separately like so:
        
        #self.fuse = fuse
        
        #To add scaling based on level:
        #self.stat[Stats.FUSE] = fuse

        # Should look simular to this:
        #def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg, fuse):
        #   super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)
        #   self.stat[Stats.FUSE] = fuse


    def attack_options(self, team):
    #What options the mob has to attack with.

        target = random.choice(team)
        #Self enclosed variable for who the attack is targeting.

        self.attack(target, 1, 0, 0)
        #
        #
        #DEFENCE ignore: 1 = 100% Defence ignore | 0.5 = 50% Defence igonre ect..


