#
# iterate_game.py
# 
#
import battlefield.item as item

class Game:

    shop = [item.HealthPotion('Health Potion', 1, 100, 0.1, item.ItemTypes.CONSUMABLE),item.HealthPotion('Great Health Potion', 1, 200, 0.33, item.ItemTypes.CONSUMABLE),item.HealthPotion('Greatest Health Potion', 1, 300, 0.45, item.ItemTypes.CONSUMABLE),item.HealthPotion('Omegus Healus', 1, 500, 0.76, item.ItemTypes.CONSUMABLE)]


    class State:
        USER_CREATE = 0
        IDLE = 1
        BATTLE = 2
        SHOP = 3
        SHOP_SELECT = 4
        DUNGEON = 5

    uid = -1
    def uid_increment():
        Game.uid +=1
        return Game.uid

    def __init__(self) -> None:
        pass

    def iterate(self, cmd):
        state = self.states[-1]
        cmd = str(cmd).lower()
        game_output = []

        if state == Game.State.IDLE:
            if cmd == 's': # If the input is (S) opens the shop
                self.states.append(Game.State.SHOP)

                output = []
                num = 0
                for i in Game.shop:
                    num += 1
                    output = output + [f'{num}. {i.name}']

                game_output = game_output + [f'Welcome to the shop!', f'what would you like to buy?',]
                for i in output:
                    game_output = game_output + [i]
                game_output = game_output + [f'Exit (x)', '']
            
            else:
                game_output = [f'{cmd} is not an option.\n']

        elif state == Game.State.SHOP:
            if cmd == 'x':
                self.states.pop(-1)
                game_output = game_output + [f'You left the shop...', '']

            else:
                pass

        else:
            self.states.append(Game.State.IDLE)
            game_output = [f'{cmd} what? how dod you get here.']
        
        return game_output

        
class PlayerTest:
    def __init__(self, states) -> None:
        self.states = states


if __name__ =='__main__':

    p = PlayerTest()


    p.states.append(Game.State.IDLE)

    while True:
        print(Game.iterate(p, input("SUS: ")))

    

