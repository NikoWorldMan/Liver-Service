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
    CURRENT_DEF = "CDEF"
    SPEED = "SPD"
    CRITRATE = "CRIT Rate"
    CRITDMG = "CRIT DMG"
    FUSE = "FUSE"

class Attack:
    SINGLE = "Single Target"
    AREA = "Single and Adjacent Target"
    FIELD = "All Targets"
    RANDOM = "Random Targets"


class Entity: # Default attributes all entities possess
    def __init__(self, name, level, health, attack, defence, speed, critrate, critdmg):


        self.turn_value: int = 0
        self.overflow_value: int = 0
        
        self.maxlv: int = 90
        self.name = str(name)
        self.level = level
        self.stats = dict()
        self.buffs: list = []

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

    def list_stats(self) -> list[str]:
        self.set_stats()

        output = [f'{self.name}\'s stats:']
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
            
            output += [stats]
        return output + ['']

        

    def clone(self):
        return copy.deepcopy(self)

    def set_stats(self):
        self.stat = self.get_true_stats()
        #self.display_health()

    def display_health(self) -> list[str]:
        return [f"Lv. {self.level} {self.name} ( {self.health} / {self.stat[Stats.HEALTH]} )"]

    def get_true_stats(self):

        mod_stat = self.stats.copy()

        for buff in self.buffs:
            try:
                if buff in self.buffs.Types:
                    if buff.stat in self.stats:
                        mod_stat[buff.stat] *= buff.amount
            except:
                print(f"WARN: {buff} not in entity.stat pool")

        return mod_stat
    
    def alive(self):
        return True if Stats.HEALTH in self.stats and self.health > 0 else False
    
    def crit_hit(self):
        return True if self.stat[Stats.CRITRATE] > random.randrange(0, 100) else False
    def crit_dmg(self):
        return ( self.stat[Stats.CRITDMG] / 100 )
    
    def damage_reduction(self, attacker, def_mult: float) -> float:
        defence = self.stat[Stats.DEFENCE] * def_mult
        levelDiff: int = 0
        if attacker.level > self.level:                                                   
            levelDiff = attacker.level - self.level
        return 1-(defence / (defence+4000 + 1500*levelDiff))

    def change_health(self, amount):
        if "HP" in self.stats:
            self.health += amount
            if self.health > self.stat[Stats.HEALTH]:
                self.health = self.stat[Stats.HEALTH]
            if self.health < 0:
                self.health = 0
        else:
            pass

    def attack(self, target, mult, add, def_ignore: float):
        damage_variance = random.randrange(98, 102)/100
        output: list[int] = []
        crit: int = 1

        if self.crit_hit():
            crit += self.crit_dmg()
            output.extend[f" - > CRIT < - "]

        damage=round((self.stat[Stats.ATTACK]*mult+add) * crit * target.damage_reduction(self, def_ignore) * damage_variance+0.5)
        output.extend[f"Lv. {self.level} {self.name} dealt {damage} damage to {target.name} (Lv. {target.level})", '']

        target.change_health(damage*-1)
        output.extend[target.display_health()]

        return output

    def attack_options(self, team):

        target = random.choice(team)
        self.attack(target, 1, 0)
        if target.alive() == False:
            print(f"Lv. {target.level} {target.name} died.")
            team.remove(target)


    def get_action_value(self, turn_cycle) -> int:
        return turn_cycle/self.stat[Stats.SPEED]
    
    def change_action_value(self, flat_amount: int, amount: float, turn_cycle) -> list[str]:
        """
        Change action value, based on base action value and/or a flat amount
        Lower action value means you go faster.
        Use a "-" infront of the int to decrease value instead of increase
        """
        base_action_value = self.get_action_value(turn_cycle)
        turn_value_change = (base_action_value * amount) + flat_amount

        if turn_value_change > 0:
            output =  [f'{self.name}\'s Action was delayed by { (turn_value_change/base_action_value) * 100 }%']
        else:
            output =  [f'{self.name}\'s Action was advanced by { (turn_value_change/base_action_value) * -100 }%']

        self.turn_value += turn_value_change

        return output
    