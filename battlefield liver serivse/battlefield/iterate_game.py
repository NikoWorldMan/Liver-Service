#
# iterate_game.py
# 
#
import battlefield.item as item
from battlefield.entity import Stats
import battlefield.shop as shop

class Game:
    """
    
    """
    turn_cycle = 10000

    shop = shop.Shop('Shop',1 , [
        item.HealthPotion('Health Potion', 2, 100, 0.1, item.ItemTypes.CONSUMABLE, 10, 1),
        item.HealthPotion('Great Health Potion', 3, 200, 0.33, item.ItemTypes.CONSUMABLE, 20, 1),
        item.HealthPotion('Greatest Health Potion', 4, 300, 0.45, item.ItemTypes.CONSUMABLE, 30, 1),
        item.HealthPotion('Omegus Healus', 5, 500, 0.76, item.ItemTypes.CONSUMABLE, 40, 1),
        item.Items('Dungeon Key', 1, item.ItemTypes.ITEM, 35, 0)
        ])


    class State:
        PAUSE = 0
        USER_CREATE = 1
        IDLE = 2
        SHOP = 3
        INVENTORY = 4
        FIGHT = 5
        DUNGEON = 10

    uid = -1
    def uid_increment():
        Game.uid +=1
        return Game.uid
    


    def dungeon_iterate(self):
        output: list[str] = []
        #if 1 in self.inv:
        if item.Items('Dungeon Key', any, any, any, any) in self.inv:
            output.extend([f'Please select dungeon type: Random Dungeon (R) | CO-OP Dungeon (M) | Exit (X)'])
            self.states.append(Game.State.DUNGEON)

        else:
            output.extend([f'You need a Dungeon key to proceed!'])
            output.extend(Game.state_info(self, []))



        return output



    def inventory_iterate(self):
        output: list[str] = [f'{self.name}\'s inventory: {self.get_inventory_space([item.ItemTypes.ITEM, item.ItemTypes.CONSUMABLE])}/{self.item_space}']
        self.states.append(Game.State.INVENTORY)

        num: int = 0
        output.extend([f'Items:'])
        for i in self.inv:
            if i.type == item.ItemTypes.ITEM:
                num += 1
                output.extend([f'{num}. {i.display()}'])

        num: int = 0
        output.extend([f'', f'Consumable:'])
        for i in self.inv:
            if i.type == item.ItemTypes.CONSUMABLE:
                num += 1
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
            items += [f'{num}. {i.name} (x{i.count}) | Cost {int(i.price*shop.price_mult)} Diamonds']

        output.extend([f'Welcome to the shop!', f'',])
        for i in items:
            output.extend([i])

        output.extend(['', f'what would you like to buy? Exit (x)'])

        return output

    def stats_iterate(self) -> list[str]:
        output: list[str] = []
        output.extend(self.list_stats())

        output.extend(Game.state_info(self, []))

        return output

    def fight_iterate(self) -> list[str]:
        output: list[str] = []
        self.states.append(Game.State.FIGHT)

        output.extend([f'Please select battle type: Random Encounter (R) | Matchmaking (M) | Exit (X)'])

        return output
    
    def shop_state(self, cmd) -> list[str]: # Shop state
        output: list[str] = []
        num: list[str] = []
        cunt: int = 0
        shop = Game.shop

        for i in shop.items:
            cunt+=1
            num.append(str(cunt))

        if cmd in num:
            the_item = shop.items[int(cmd)-1]
            price: int = int(the_item.price * shop.price_mult)
            if self.currency >= price:  
                self.collect_item(the_item)
                output.extend(['', f'You bought {the_item.name}'])
                self.currency -= price
            else:
                output.extend([f'You do not have enough Diamonds to buy this item!'])

            output.extend(Game.state_info(self, []))
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
        elif cmd == 'd':
            output += Game.dungeon_iterate(self)
        else:
            output += [f'Please enter a valid option...']

        #output.extend(Game.state_info(self, []))
        return output

    def inventory_state(self, cmd) -> list[str]:
        output: list[str] = []

        if cmd == 'x':
            self.states.pop(-1) # Goes back to the previous state
            output.extend(Game.state_info(self, [f'You closed you\'r inventory...']))
        else:
            output.extend(['', f'Please enter a valid option...'])
            output.extend(Game.state_info(self, []))

        return output
    

    def dungeon_state(self, cmd) -> list[str]:
        output: list[str] = []

        if cmd == 'x':
            self.states.pop(-1)
            output.extend(Game.state_info(self, [f'You left the dungeon']))
        else:
            output.extend(['', f'Please enter a valid option...'])

        output.extend(Game.state_info(self, []))
        return output

    def fight_state(self, cmd) -> list[str]:
        output: list[str] = []

        if cmd == 'x':
            self.states.pop(-1)
            output.extend(Game.state_info(self, [f'You stopped searching for a fight']))


    def iterate(player, cmd) -> list[str]:
        state = player.states[-1]
        cmd = str(cmd).lower()
        output: list[str] = []

        if state == Game.State.IDLE:
            output.extend(Game.idle_state(player, cmd))
        elif state == Game.State.SHOP:
            output.extend(Game.shop_state(player, cmd))
        elif state == Game.State.INVENTORY:
            output.extend(Game.inventory_state(player, cmd))
        elif state == Game.State.DUNGEON:
            output.extend(Game.dungeon_state(player, cmd))
        elif state == Game.State.FIGHT:
            output.extend(Game.fight_state(player, cmd))
        else:
            #self.states.append(Game.State.IDLE)
            output += [f'{cmd} what? how did you get here.']
        
        return output
    
    def state_info(self, current_state_leave_message: list[str]) -> list[str]:
        output: list[str] = ['']
        state = self.states[-1]

        if state == Game.State.IDLE:
            output.extend([f'What to you want to do now?', f'Shop (S) | Fight (F) | Dungeon (D) | Stats (T) | Inventory (I) | ', ''])
        elif state == Game.State.DUNGEON:
            output.extend([f'Please select dungeon type: Random Dungeon (R) | CO-OP Dungeon (M) | Exit (X)'])
        elif state == Game.State.INVENTORY:
            output.extend(Game.inventory_iterate(self))
            self.states.pop(-1)
        elif state == Game.State.SHOP:
            output.extend(Game.shop_iterate(self))
            self.states.pop(-1)
        else:
            output.extend(current_state_leave_message)
        return output

        

# ///////////////////////
if __name__ =='__main__':

    while True:
        print(Game.iterate('player', input("Command?")))