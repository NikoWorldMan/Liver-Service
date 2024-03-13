#
# iterate_game.py
# 
#
import battlefield.item as item
from battlefield.entity import Stats
import battlefield.shop as shop

class Game:
    turn_cycle = 10000

    shop = shop.Shop('Shop',1 , [
        item.HealthPotion('Health Potion', 1, 100, 0.1, item.ItemTypes.CONSUMABLE, 10),
        item.HealthPotion('Great Health Potion', 1, 200, 0.33, item.ItemTypes.CONSUMABLE, 20),
        item.HealthPotion('Greatest Health Potion', 1, 300, 0.45, item.ItemTypes.CONSUMABLE, 30),
        item.HealthPotion('Omegus Healus', 1, 500, 0.76, item.ItemTypes.CONSUMABLE, 40)
        ])


    class State:
        USER_CREATE = 0
        IDLE = 1
        SHOP = 2
        INVENTORY = 3
        FIGHT = 4



    uid = -1
    def uid_increment():
        Game.uid +=1
        return Game.uid

    def __init__(self) -> None:
        pass

    def inventory_iterate(self):
        output: list[str] = [f'{self.name}\'s inventory']
        self.states.append(Game.State.INVENTORY)

        num: int = 0
        output.extend([f'Items:'])
        for i in self.inv:
            num += 1
            if i.type == item.ItemTypes.ITEM:
                output.extend([f'{num}. {i.display()}'])

        num: int = 0
        output.extend([f'', f'Consumable:'])
        for i in self.inv:
            num += 1
            if i.type == item.ItemTypes.CONSUMABLE:
                output.extend([f'{num}. {i.display()}'])

        output.extend([f'', f'What item would you like to use? Exit (x)', f''])


        return output

    def shop_iterate(self) -> list[str]:
        output: list[str] = []
        self.states.append(Game.State.SHOP)
        shop = Game.shop
        items = []
        num = 0
        for i in shop.items:
            num += 1
            items += [f'{num}. {i.name} | Cost {int(i.price*shop.price_mult)} Diamonds']

        output += [f'Welcome to the shop!', f'what would you like to buy? Exit (x)',]
        for i in items:
            output.extend([i])
        return output + ['']

    def stats_iterate(self) -> list[str]:
        output: list[str] = []
        output.extend(self.list_stats())
        return output

    def fight_iterate(self) -> list[str]:
        output: list[str] = []
        self.states.append(Game.State.FIGHT)



        return output
    
    def shop_state(self, cmd) -> list[str]: # Shop state
        output: list[str] = []
        output.extend(Game.shop_iterate(self))
        self.states.pop(-1)
        
        num: list[str] = []
        count: int = 0
        shop = Game.shop

        for i in shop.items:
            count+=1
            num.append(str(count))

        if cmd in num:
            the_item = shop.items[int(cmd)-1]
            price: int = int(the_item.price*shop.price_mult)
            if self.currency >= price:
                self.collect_item(self.inv, the_item)
                output.extend(['', f'You bought {the_item.name}'])
                self.currency -= price
            else:
                output.extend([f'You do not have enough Diamonds to buy this item!'])

            return output

        if cmd == 'x':
            self.states.pop(-1) # Goes back to the previous state
            output.extend(Game.state_info(self, [f'You left the shop...']))
        else:
            output.extend(['', f'Please enter a valid option...'])

        return output


    def idle_state(self, cmd) -> list[str]: # Idle state,
        output: list[str] = []
        if cmd == 's': # If the input is (S) opens the shop
            output += Game.shop_iterate(self)
        elif cmd == 'f': # If the input is (F) opens the fight selector
            output += Game.fight_iterate(self)
        elif cmd == 't':
            output += Game.stats_iterate(self)
        elif cmd == 'i':
            output += Game.inventory_iterate(self)
        else:
            output += [f'{cmd} is not an option.\n']
        return output

    def inventory_state(self, cmd) -> list[str]:
        output: list[str] = []
        if cmd == 'x':
            self.states.pop(-1) # Goes back to the previous state
            output.extend(Game.state_info(self, [f'You closed you\'r inventory...']))
        else:
            output.extend(['', f'Please enter a valid option...'])

        return output

    def iterate(self, cmd) -> list[str]:
        state = self.states[-1]
        cmd = str(cmd).lower()
        output: list[str] = []

        if state == Game.State.IDLE:
            output.extend(Game.idle_state(self, cmd))
        elif state == Game.State.SHOP:
            output.extend(Game.shop_state(self, cmd))
        elif state == Game.State.INVENTORY:
            output.extend(Game.inventory_state(self, cmd))
        else:
            #self.states.append(Game.State.IDLE)
            output += [f'{cmd} what? how did you get here.']
        
        return output
    
    def state_info(self, current_state_leave_message: list[str]) -> list[str]:
        output: list[str] = ['']
        state = self.states[-1]

        if state == Game.State.IDLE:
            output.extend([f'What to you want to do now?', f'Shop (S) | Fight (F) | Dungeon (D) | Inventory (I) | '])
        else:
            output.extend(current_state_leave_message)
        return output

        
# ///////////////////////
if __name__ =='__main__':

    Game.iterate()