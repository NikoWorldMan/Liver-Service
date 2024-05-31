
#
# player.py
# player class
#

# Imports
import time
import random
import battlefield.entity as entity
import battlefield.item as items
import battlefield.weapons as weapons
from battlefield.item import ItemTypes
from battlefield.entity import Stats
from battlefield.entity import Stat as EntityStat
from battlefield.iterate_game import Game as Game
import math
from dataclasses import dataclass

@dataclass
class Stat(EntityStat):
    upgrade_mult: int = 1

class Player(entity.Entity):  
    type = 'Player' 
    def __init__(self, name=str, level=int, health=Stat, attack=Stat, defence= Stat, speed=Stat, critrate=Stat, critdmg=Stat, stamina=Stat, item_space=int, weapon_space=int, currency=int, xp=int, xpmax=int):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)

        self.states = [Game.State.IDLE]
        self.using_skill = None
        self.weapon = None

        self.upgrading_stats = []
        self.stat[Stats.STAMINA] = stamina
        self.set_stats()
        self.stamina = self.stat[Stats.STAMINA].stat

        self.maxlv: int = 80
        self.level_iterations = 10
        self.stat_max_upgrades_per_level_iteration = 4

        self.xp: float = xp
        self.xpmax: float = xpmax

        self.inv: list = []
        self.biome = None

        self.item_space = item_space
        self.weapon_space = weapon_space
        self.currency = currency

    def level_up(self):

        if self.level % 10 == 0:
            for stat in self.stat:
                stat = self.stat[stat]
                stat.upgrade_count = self.stat_max_upgrades_per_level_iteration

        if len(self.upgrading_stats) < 1:
            upgrading_stats = []
            for i in self.stat:
                s = self.stat[i]
                if s.upgrade_count > 0:
                    upgrading_stats.append(i)

            for i in range(1, 4):
                b = random.choice(upgrading_stats)
                self.upgrading_stats.append(b)
                upgrading_stats.remove(b)


    def display_health(self) -> list[str]:
        return [f"Lv. {self.level} {self.name} '{self.type}' ( {int(self.health)} / {int(self.stat[Stats.HEALTH].stat)} )"]

    def list_stats(self) -> list[str]:
        self.set_stats()

        output = [f"{self.name} - {self.type} Lv. {self.level}"]
        stats: list = []

        line = "-" * ( len(output[0]) -1 )

        stats.extend([f'XP: {int(self.xp)} / {int(self.xpmax)}', f' {line} '])

        if Stats.HEALTH in self.stat:
            stats.extend([f"- {Stats.HEALTH}: {int(self.health)} / {int(self.stat[Stats.HEALTH].stat)}"])
        if Stats.STAMINA in self.stat:
            stats.extend([f"- {Stats.STAMINA}: {int(self.stamina)} / {int(self.stat[Stats.STAMINA].stat)}"])
        if Stats.MANA in self.stat:
            stats.extend([f"- {Stats.MANA}: {int(self.mana)} / {int(self.stat[Stats.MANA].stat)}"])
        if Stats.ATTACK in self.stat:
            stats.extend([f"- {Stats.ATTACK}: {int(self.stat[Stats.ATTACK].stat)}"])
        if Stats.DEFENCE in self.stat:
            stats.extend([f"- {Stats.DEFENCE}: {int(self.stat[Stats.DEFENCE].stat)} "])
        if Stats.SPEED in self.stat:
            stats.extend([f"- {Stats.SPEED}: {int(self.stat[Stats.SPEED].stat)}"])
        if Stats.CRITRATE in self.stat:
            stats.extend([f"- {Stats.CRITRATE}: {round(self.stat[Stats.CRITRATE].stat, 1)} %"])
        if Stats.CRITDMG in self.stat:
            stats.extend([f"- {Stats.CRITDMG}: {round(self.stat[Stats.CRITDMG].stat, 1)} %"])

        output.extend(stats)
        return output + ['']


    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xpmax:
            self.states.append(Game.State.LEVEL_UP)
            self.xp -= self.xpmax
            self.xpmax += self.xpmax/25 + 5

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

    def collect_item(self, item):

        for i in self.inv:
            if i.name == item.name:
                i.count += item.count
                return

        self.inv.append(item.clone())
   

class Magic(Player):
    type = 'Magic'
    def __init__(self, name=str, level=int, health=Stat, mana=Stat, attack=Stat, defence=Stat, speed=Stat, critrate=Stat, critdmg=Stat, stamina=Stat, item_space=int, weapon_space=int, currency=int, xp=int, xpmax=int):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg, stamina, item_space, weapon_space, currency, xp, xpmax)

        self.stat[Stats.MANA] = mana
        self.set_stats()
        self.mana = self.stat[Stats.MANA].stat


class Templar(Player):
    type = 'Templar'
    desc = 'Posesses powerful attacks and shielding abilities'
    ability_info = 'Notable skills:\n- All attacks ignore some DEF and delays the enemy'

class Necromancer(Magic):
    def __init__(self, name=str, level=int, health=Stat, mana=Stat, attack=Stat, defence=Stat, speed=Stat, critrate=Stat, critdmg=Stat, stamina=Stat, item_space=int, weapon_space=int, currency=int, xp=int, xpmax=int):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg, stamina, item_space, weapon_space, currency, xp, xpmax)
    type = 'Necromancer'
    desc = "Summons minions to aid in battles"
    ability_info = 'Notable skills:, Can summon monsters half i\'ts level'
        

class Psion(Player):
    type = 'Psion'
    desc = 'Has the power of mind control'
    ability_info = 'Notable skills: High speed, Life steal, Can make decoys of itself'

class Blightbringer(Magic):
    def __init__(self, name=str, level=int, health=Stat, mana=Stat, attack=Stat, defence=Stat, speed=Stat, critrate=Stat, critdmg=Stat, stamina=Stat, item_space=int, weapon_space=int, currency=int, xp=int, xpmax=int):
        super().__init__(name, level, health, mana, attack, defence, speed, critrate, critdmg, stamina, item_space, weapon_space, currency, xp, xpmax)
    type = 'Mage'
    desc = "Access to powerful spells, but has low speed"
    ability_info = 'Notable skills: Apply debuffs to enemies'

    def create_weapon(self, rarity: int, name: str | None):
        """
        rarity = 1 / 2 / 3
        Choosing any other number will cause the weapon to be of random rarity
        """

        
        if name is None:
            ...

        weapon = weapons.Weapon(ItemTypes.WEAPON)


class SetClasses:
     def mage() -> list[str]:
        new_player = Blightbringer(name=None, level=1, health=Stat(base=450, scaleing=200, base_scaleing=16, upgrade_mult=70), mana=Stat(base=50, scaleing=50, base_scaleing=1, upgrade_mult=33.4375), attack=Stat(base=250, scaleing=70, base_scaleing=10, upgrade_mult=20), defence=Stat(base=310, scaleing=140, base_scaleing=12, upgrade_mult=45), speed=Stat(base=89, scaleing=1.2, base_scaleing=0.08, upgrade_mult=0.9), critrate=Stat(base=9, scaleing=1, base_scaleing=0.1538, upgrade_mult=0.8), critdmg=Stat(base=47.5, scaleing=2.5, base_scaleing=1, upgrade_mult=2.5), stamina=Stat(base=115, scaleing=3, base_scaleing=3, upgrade_mult=6), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player
     
     def templar() -> list[str]:
        new_player = Templar(name=None, level=1, health=Stat(base=650, scaleing=250, base_scaleing=20.77, upgrade_mult=100), attack=Stat(base=270, scaleing=50, base_scaleing=11, upgrade_mult=25), defence=Stat(base=200, scaleing=80, base_scaleing=14, upgrade_mult=30), speed=Stat(base=94, scaleing=1.5, base_scaleing=0.19, upgrade_mult=0.92), critrate=Stat(base=13, scaleing=2, base_scaleing=0.25, upgrade_mult=0.5), critdmg=Stat(base=47.5, scaleing=2.5, base_scaleing=0.3, upgrade_mult=3), stamina=Stat(base=99, scaleing=1, base_scaleing=5, upgrade_mult=7), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player
     
     def psion() -> list[str]:
        new_player = Psion(name=None, level=1, health=Stat(base=450, scaleing=180, base_scaleing=14, upgrade_mult=60), attack=Stat(base=245, scaleing=55, base_scaleing=9, upgrade_mult=16), defence=Stat(base=1150, scaleing=150, base_scaleing=16, upgrade_mult=65), speed=Stat(base=103, scaleing=2, base_scaleing=0.25, upgrade_mult=1.1), critrate=Stat(base=5.8, scaleing=2.2, base_scaleing=0.0354, upgrade_mult=1), critdmg=Stat(base=46.5, scaleing=3.5, base_scaleing=0.25, upgrade_mult=2), stamina=Stat(base=154, scaleing=6, base_scaleing=4, upgrade_mult=9), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player
     
     def necromancer() -> list[str]:
        new_player = Necromancer(name=None, level=1, health=Stat(base=500, scaleing=180, base_scaleing=15, ), mana=Stat(base=40, scaleing=20, base_scaleing=1, upgrade_mult=16), attack=Stat(base=200, scaleing=35, base_scaleing=7, upgrade_mult=12), defence=Stat(base=450, scaleing=150, base_scaleing=12, upgrade_mult=50), speed=Stat(base=99, scaleing=1.15, base_scaleing=0.3, upgrade_mult=1), critrate=Stat(base=5, scaleing=0, base_scaleing=0.215, upgrade_mult=1.2), critdmg=Stat(base=37.5, scaleing=2.5, base_scaleing=0.5, upgrade_mult=2), stamina=Stat(base=57, scaleing=3, base_scaleing=2.5, upgrade_mult=4), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player

classes = [Blightbringer, Necromancer, Psion, Templar]

