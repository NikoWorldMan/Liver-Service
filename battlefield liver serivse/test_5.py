import math
class Character:
    def __init__(self, level, health, health_scaleing, extra) -> None:
        self.level = level
        self.health = health
        self.health_scaleing = health_scaleing
        self.increase = extra * (health_scaleing + 1)
        self.max_level = 80

    def get_max_stat(self, stat):
        stat = stat

        max = 0
        current = (self.increase + self.health + (self.level * self.health_scaleing))

        iteration =(math.floor(self.level / 10) + 1)*8

        max = (((iteration) + (self.health + self.health_scaleing * iteration))) * 1.2


        pass
        print(f'Max: {int(max)}')
        print(f'Current {int(current)}')


player = Character(level=80, health=100, health_scaleing=0.2, extra=15)

player.get_max_stat(2)