#
# iterate_game.py
# 
#
import battlefield.item as item
from battlefield.entity import Stats

class Game:

    shop = [item.HealthPotion('Health Potion', 1, 100, 0.1, item.ItemTypes.CONSUMABLE),item.HealthPotion('Great Health Potion', 1, 200, 0.33, item.ItemTypes.CONSUMABLE),item.HealthPotion('Greatest Health Potion', 1, 300, 0.45, item.ItemTypes.CONSUMABLE),item.HealthPotion('Omegus Healus', 1, 500, 0.76, item.ItemTypes.CONSUMABLE)]


    class State:
        USER_CREATE = 0
        IDLE = 1
        SHOP = 2
        FIGHT =3
        BATTLE = 4
        SHOP_SELECT = 5
        DUNGEON = 6

    uid = -1
    def uid_increment():
        Game.uid +=1
        return Game.uid

    def __init__(self) -> None:
        pass


    def shop_iterate(self) -> list[str]:
        self.states.append(Game.State.SHOP)

        output = []
        items = []
        num = 0
        for i in Game.shop:
            num += 1
            items += [f'{num}. {i.name}']

        output += [f'Welcome to the shop!', f'what would you like to buy?',]
        for i in items:
            output = output + [i]
        return output + [f'Exit (x)', '']


    def fight_iterate(self) -> list[str]:
        self.states.append(Game.State.FIGHT)

        output: list[str] = []

        return output
    
    def shop_state(self, cmd) -> list[str]: # Shop state
        output: list[str] = []
        if cmd == 'x':
            self.states.pop(-1)
            output += [f'You left the shop...', '']
        return output

    def idle_state(self, cmd) -> list[str]: # Idle state,
        output: list[str] = []
        if cmd == 's': # If the input is (S) opens the shop
            output += Game.shop_iterate(self)
        elif cmd == 'f': # If the input is (F) opens the fight selector
            output += Game.fight_iterate(self)
        elif cmd == 't':
            output += Game.stats_iterate(self)
        else:
            output += [f'{cmd} is not an option.\n']
        return output

    def stats_iterate(self) -> list[str]:
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

    def iterate(self, cmd) -> list[str]:
        state = self.states[-1]
        cmd = str(cmd).lower()

        output: list[str] = []

        if state == Game.State.IDLE:
            return Game.idle_state(self, cmd)

        elif state == Game.State.SHOP:
            return Game.shop_state(self, cmd)

        else:
            #self.states.append(Game.State.IDLE)
            output += [f'{cmd} what? how did you get here.']
        
        return output

        
class PlayerTest:
    def __init__(self, states):
        self.states = states


# ///////////////////////
if __name__ =='__main__':

    p = PlayerTest()


    p.states.append(Game.State.IDLE)

    while True:
        print(Game.iterate(p, input("SUS: ")))

