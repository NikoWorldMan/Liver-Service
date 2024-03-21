
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
from battlefield.entity import Stat
from battlefield.iterate_game import Game




class Player(entity.Entity):  
    type = 'Player' 
    def __init__(self, name=str, level=int, health=Stat, attack=Stat, defence= Stat, speed=Stat, critrate=Stat, critdmg=Stat, stamina=Stat, item_space=int, weapon_space=int, currency=int, xp=int, xpmax=int):
        super().__init__(name, level, health, attack, defence, speed, critrate, critdmg)

        self.states = [Game.State.IDLE]
        self.using_skill = None
        self.weapon = None

        self.stat[Stats.STAMINA] = stamina
        self.set_stats()
        self.stamina = self.stat[Stats.STAMINA].stat

        self.maxlv: int = 90
        self.level_iterations = 10
        self.stat_max_upgrades_per_level_iteration = 4

        self.xp: float = xp
        self.xpmax: float = xpmax

        self.inv: list = []
        self.biome = None

        self.item_space = item_space
        self.weapon_space = weapon_space
        self.currency = currency

    def display_health(self) -> list[str]:
        return [f"Lv. {self.level} {self.name} '{self.type}' ( {int(self.health)} / {int(self.stat[Stats.HEALTH].stat)} )"]

    def list_stats(self) -> list[str]:
        self.set_stats()

        output = [f"{self.name} - {self.type} Lv. {self.level}"]
        stats: list = []

        line = "-" * ( len(output[0]) -1 )

        stats.extend([f'XP: {self.xp} / {self.xpmax}', f' {line} '])

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
        new_player = Blightbringer(name=None, level=1, health=Stat(base=450, scaleing=200, base_scaleing=16), mana=Stat(base=50, scaleing=50, base_scaleing=5), attack=Stat(base=250, scaleing=100, base_scaleing=14), defence=Stat(base=300, scaleing=150, base_scaleing=15), speed=Stat(base=97, scaleing=1, base_scaleing=0.3), critrate=Stat(base=9, scaleing=1, base_scaleing=0.5), critdmg=Stat(base=55, scaleing=5, base_scaleing=5), stamina=Stat(base=450, scaleing=150, base_scaleing=7), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player
     
     def templar() -> list[str]:
        new_player = Templar(name=None, level=1, health=Stat(base=650, scaleing=250, base_scaleing=20), attack=Stat(base=270, scaleing=70, base_scaleing=16), defence=Stat(base=200, scaleing=80, base_scaleing=14), speed=Stat(base=95, scaleing=1, base_scaleing=0.35), critrate=Stat(base=13, scaleing=2, base_scaleing=0.5), critdmg=Stat(base=45, scaleing=5, base_scaleing=3.8), stamina=Stat(base=99, scaleing=1, base_scaleing=11), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player
     
     def psion() -> list[str]:
        new_player = Psion(name=None, level=1, health=Stat(base=450, scaleing=180, base_scaleing=14), attack=Stat(base=300, scaleing=80, base_scaleing=15), defence=Stat(base=1000, scaleing=150, base_scaleing=15), speed=Stat(base=108, scaleing=2, base_scaleing=0.45), critrate=Stat(base=0, scaleing=5, base_scaleing=0.33), critdmg=Stat(base=42, scaleing=8, base_scaleing=2), stamina=Stat(base=174, scaleing=6, base_scaleing=8), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player
     
     def necromancer() -> list[str]:
        new_player = Necromancer(name=None, level=1, health=Stat(base=500, scaleing=180, base_scaleing=15), mana=Stat(base=40, scaleing=25, base_scaleing=5), attack=Stat(base=200, scaleing=50, base_scaleing=10), defence=Stat(base=450, scaleing=150, base_scaleing=15), speed=Stat(base=99, scaleing=1, base_scaleing=0.4), critrate=Stat(base=5, scaleing=1, base_scaleing=0.8), critdmg=Stat(base=45, scaleing=5, base_scaleing=1), stamina=Stat(base=57, scaleing=3, base_scaleing=5), item_space= 20, weapon_space= 5, currency= 100, xp=0, xpmax=100)
        return new_player

classes = [Blightbringer, Necromancer, Psion, Templar]

