import math

class Character:
    def __init__(self, level, stat, stat_scaleing, extra) -> None:
        self.level = level
        self.stat = stat
        self.stat_scaleing = stat_scaleing
        self.increase = extra * (stat_scaleing + 1)
        self.max_level = 80

    def get_max_stat(self):

        iteration = math.floor(4*(self.level/10))

        phase = (self.level/10)

        max = self.stat + ( self.stat_scaleing * (phase - 1)) + iteration        

        current = self.stat + (self.stat_scaleing * self.level)

        print(f'Max: {int(max)}')
        print(f'Current: {int(current)}')


player = Character(1, 100, 1, 0)

player.get_max_stat()