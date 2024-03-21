#
# entity.py
#
from dataclasses import dataclass
import copy
import random

class Stats:
    HEALTH = "HP"
    MANA = "MP"
    ATTACK = "ATK"
    DEFENCE = "DEF"
    CURRENT_DEF = "CDEF" # Hidden stat
    SPEED = "SPD"
    CRITRATE = "CRIT Rate"
    CRITDMG = "CRIT DMG"
    FUSE = "FUSE"
    STAMINA = "STM"
@dataclass
class Stat:
    base: int = 1
    scaleing: int = 0
    base_scaleing: int = 0
    extra: int = 0
    upgrade_count: int = 4


class Attack:
    SINGLE = "Single Target"
    AREA = "Single and Adjacent Target"
    FIELD = "All Targets"
    RANDOM = "Random Targets"


class Entity: # Default attributes all entities possess
    type = 'Entity'
    def __init__(self, name, level, health=Stat, attack=Stat, defence=Stat, speed=Stat, critrate=Stat, critdmg=Stat):
        """
        Stats Scaleing: [ BASE ;- SCALEING ;- BASE_SCALEING ]
        """

        self.fight_id = None
        self.turn_value: int = 0
        self.overflow_value: int = 0

        self.name = str(name)
        self.level = level
        self.buffs: list = []

        self.stat = dict()


        self.stat[Stats.HEALTH] = health
        self.stat[Stats.ATTACK] = attack
        self.stat[Stats.DEFENCE] = defence
        self.stat[Stats.SPEED] = speed
        self.stat[Stats.CRITRATE] = critrate
        self.stat[Stats.CRITDMG] = critdmg



        self.health = 0
        self.set_stats()
        self.health = self.stat[Stats.HEALTH].stat


    def list_stats(self) -> list[str]:
        output: list[str] = []
        self.set_stats()

        return output + ['']

    def clone(self):
        return copy.deepcopy(self)

    def set_stats(self):
        self.set_base_stats()
        #self.display_health()

    def display_health(self) -> list[str]:
        return [f"Lv. {self.level} {self.name} ( {int(self.health)} / {int(self.stat[Stats.HEALTH].stat)} )"]

    def set_base_stats(self):

        for i in self.stat:
            stat = self.stat[i]

            stat.stat = stat.base + stat.scaleing * (self.level / (self.level ** 0.33)) + stat.base_scaleing * (self.level - 1)
            stat.stat += stat.extra

        if Stats.CRITRATE in self.stat:
            if self.stat[Stats.CRITRATE].stat > 100:
                self.stat[Stats.CRITRATE].stat = 100
                self.stat[Stats.CRITDMG].stat += (self.stat[Stats.CRITRATE].stat - 100) * 1.8

    def get_true_stats(self):
        mod_stat = self.stats.copy()

        for buff in self.buffs:
            try:
                if buff in self.buffs.Types:
                    if buff.stat in self.stats:
                        mod_stat[buff.stat] *= buff.amount
            except:
                pass

        return mod_stat
    
    def alive(self):
        return True if Stats.HEALTH in self.stats and self.health > 0 else False
    
    def crit_hit(self):
        return True if self.stat[Stats.CRITRATE].stat > random.randrange(0, 100) else False
    def crit_dmg(self):
        return ( self.stat[Stats.CRITDMG].stat / 100 )
    
    def damage_reduction(self, attacker, def_mult: float) -> float:
        defence = self.stat[Stats.DEFENCE].stat * def_mult
        level_dif: int = 0
        if attacker.level > self.level:                                                   
            levelDiff = attacker.level - self.level
        return 1-((1 + defence) / (defence + 500 + (2 ** level_dif) + 66 * level_dif ))
    


    def change_health(self, amount):
        if "HP" in self.stat:
            self.health += amount
            if self.health > self.stat[Stats.HEALTH].stat:
                self.health = self.stat[Stats.HEALTH].stat
            if self.health < 0:
                self.health = 0
        else:
            pass

    def attack(self, target, mult, add, def_ignore: float):
        damage_variance = random.randrange(98, 102)/100
        output: list[int] = []
        crit: int = 1
        try:
            if def_ignore >= 0:
                pass
            if def_ignore < 0:
                pass
        except:
            def_ignore = 0

        if self.crit_hit():
            crit += self.crit_dmg()
            output.extend[f" - > CRIT < - "]

        damage=round((self.stat[Stats.ATTACK].stat*mult+add) * crit * target.damage_reduction(self, def_ignore) * damage_variance+0.5)
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
        return turn_cycle/self.stat[Stats.SPEED].stat
    
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
    
