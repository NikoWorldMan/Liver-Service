#
# entity.py
#

import copy
import random

class Stats:
    HEALTH = "HP"
    MANA = "MP"
    ATTACK = "ATK"
    DEFENCE = "DEF"
    SPEED = "SPD"
    CRITRATE = "CRIT Rate"
    CRITDMG = "CRIT DMG"
    FUSE = "FUSE"


class Entity: # Default attributes all entities possess
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):
        
        self.maxlv = 90
        self.name = str(name)
        self.level = level
        self.stats = dict()
        self.buffs = []

        self.stat = dict()

        self.stats[Stats.HEALTH] = health
        self.stats[Stats.ATTACK] = attack
        self.stats[Stats.DEFENCE] = defence
        self.stats[Stats.SPEED] = speed
        self.stats[Stats.CRITRATE] = critrate
        self.stats[Stats.CRITDMG] = critdmg

        self.health = 0
        self.set_stats()
        self.health = self.stat[Stats.HEALTH]

        self.inv = []

    def list_stats(self):
        self.set_stats()
        

        print("\n[ ------------------------- ]")
        print(f"{self.name} - Level: {self.level} ( {self.xp} / {self.xpmax} )")
        for stat in self.stat:
            stats = f"- {stat}: "
            if stat == Stats.HEALTH:
                stats += f"{self.health} / {self.stat[stat]}"
            elif stat == Stats.MANA:
                stats += f"{self.mana} / {self.stat[stat]}"
            elif stat == Stats.CRITRATE:
                stats += f"{self.stat[stat]} %"
            elif stat == Stats.CRITDMG:
                stats += f"{self.stat[stat]} %"
            else:
                stats += f"{self.stat[stat]}"

            print(stats)
        print()

        

    def clone(self):
        return copy.deepcopy(self)

    def set_stats(self):
        self.stat = self.get_true_stats()
        #self.display_health()

    def display_health(self):
        print(f"Lv. {self.level} {self.name} ( {self.health} / {self.stat[Stats.HEALTH]} )")

    def get_true_stats(self):

        mod_stat = self.stats.copy()

        for buff in self.buffs:
            if buff in self.buffs.Types:
                if buff.stat in self.stats:
                    mod_stat[buff.stat] *= buff.amount

        return mod_stat
    
    def alive(self):
        return True if Stats.HEALTH in self.stats and self.health > 0 else False
    
    def crit_hit(self):
        damage = 1.1
        overcrit = 0
        while self.stat[Stats.CRITRATE] - overcrit > random.randrange(0, 100):
            overcrit += 100

            damage += self.stat[Stats.CRITDMG]/(120+(overcrit*0.6))

        if overcrit > 0:
            crit = f" - > CRIT"
            if overcrit > 100:
                crit += f" (x{int(overcrit/100)})"
            print(crit + f" < -")

        return damage
    
    def damage_reduction(self, attacker):
        levelDiff = 0
        if attacker.level > self.level:                                                   
            levelDiff = attacker.level - self.level
        return 1-(self.stat[Stats.DEFENCE]/(self.stat[Stats.DEFENCE]+4000+1500*levelDiff))

    def change_health(self, amount):
        if "HP" in self.stats:
            self.health += amount
            if self.health > self.stat[Stats.HEALTH]:
                self.health = self.stat[Stats.HEALTH]
            if self.health < 0:
                self.health = 0
        else:
            pass

    def attack(self, target, mult, add):
        damage_variance = random.randrange(95, 105)/100

        damage=round((self.stat[Stats.ATTACK]*mult+add) * self.crit_hit() * target.damage_reduction(self) * damage_variance+0.5)
        print(f"Lv. {self.level} {self.name} dealt {damage} damage to {target.name} (Lv. {target.level})\n")

        target.change_health(damage*-1)
        target.display_health()

    def attack_options(self, team):

        target = random.choice(team)
        self.attack(target, 1, 0)
        if target.alive() == False:
            print(f"Lv. {target.level} {target.name} died.")
            team.remove(target)


    def get_action_value(self, cycle_mult):
        return cycle_mult/self.stat[Stats.SPEED]
    




