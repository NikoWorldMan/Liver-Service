@property
def rfed():
    ...
from dataclasses import dataclass


class Stats:
    MANA = 'MP'
    HEALTH = 'HP'

@dataclass
class Stat:
    base: int = 1
    scaleing: int = 1


class Character:
    def __init__(self, name: str, mana= Stat, health =Stat, lvl= int) -> None:
        self.stats = dict()

        self.level = lvl
        self.name = name


        self.stats[Stats.MANA] = mana
        self.stats[Stats.HEALTH] = health




    def __str__(self) -> str:
            
        stat = self.stats[Stats.MANA]

        stat = stat.base + stat.scaleing * (self.level/ (self.level + 1)**0.33 )
        return f'{stat}'
    
    def test(self) -> str:
        output: list[str] = []

        for i in self.stats:
            stat = self.stats[i]

            stat = stat.base + stat.scaleing * (self.level/ (self.level + 1)**0.33 )

            output.extend([f'{stat}'])


        return output


player = Character('Player', mana=Stat(base=60, scaleing=10), health=Stat(base=70, scaleing=11), lvl=16 )

for i in player.test():
    print(i)


