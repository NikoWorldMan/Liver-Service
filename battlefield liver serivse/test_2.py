global active
active = True

global action_value
action_value = 1000

class Unit:
    def __init__(self, **args) -> None:
        self.name = args["name"]
        self.defence_max = args["defence"]
        self.current_def = self.defence_max
        self.atk = args["attack"]
        self.spd = args["speed"]
        self.action_value = 0

    def attack(self, target):
        self.action_value = action_value/self.spd
        target.current_def -= self.atk
        print(f'{self} dealt {self.atk} damage to {target}')
        if target.current_def < 1:
            print(f'{self} Won!!!\n')
            active == False
            exit(0)

    def __str__(self) -> str:
        return f'{self.name} ( {int(self.current_def)} / {int(self.defence_max)} )'


player = Unit(attack=2.5, defence=16, name='bob', speed=13)
enemy = Unit(attack=3, defence = 12, name='ted', speed=15)


while active:


    if player.action_value <= 0:
        input(" -------- ")
        player.attack(enemy)

    if enemy.action_value <= 0:
        input(" -------- ")
        enemy.attack(player)


    player.action_value -= 1
    enemy.action_value -=1