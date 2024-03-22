#
# iterate_game.py
# 
#
import battlefield.item as item
from battlefield.entity import Stats
from battlefield.entity import Stat
import battlefield.shop as shop
import battlefield.mobs as mobs
import battlefield.world as world
import copy
import random
import math

class Game:
    """
    
    """
    battles: list = []

    turn_cycle = 10000
    fight_id = -1

    shop = shop.Shop('Shop',1 , [
        item.HealthPotion('Health Potion', 2, 100, 0.1, 10, 1),
        item.HealthPotion('Great Health Potion', 3, 200, 0.33, 20, 1),
        item.HealthPotion('Greatest Health Potion', 4, 300, 0.45, 30, 1),
        item.HealthPotion('Omegus Healus', count=5, heal_amount=500, maxhealth_mult=0.76, price=40, storage=1),
        item.Key('Dungeon Key', 1, 35, 0),
        item.ManaPotion('Magus Drinkus', 2, 25, 0.65, 25, 1)
        ])
    
    crpr = mobs.Creeper('Crpr', 800, health=Stat(base=350, scaleing=35, base_scaleing=12), attack=Stat(base=200, scaleing=5, base_scaleing=6), defence=Stat(base=220, scaleing=8, base_scaleing=4), speed=Stat(base=103, scaleing=2, base_scaleing=0.3), critrate=Stat(base=0 ,scaleing=0 ,base_scaleing=0), critdmg=Stat(base=0, scaleing=0, base_scaleing=0), fuse=4).clone()
    
    enemies = [crpr]
    

#
    def assign_fight_id() -> int:
        Game.fight_id += 1
        return Game.fight_id

    class Fight:
        def __init__(self, team_1: list[any], team_2: list[any]) -> None:
            self.id = Game.assign_fight_id()
            self.team_1: list = team_1
            self.team_2: list = team_2

            self.team_1_defeated = []
            self.team_2_defeated = []
        
        def clone(self):
            return copy.deepcopy()
        
        def team_1_info(self):
            output: list[str] = []

            for i in self.team_1:
                output.extend(i.display_health())
            return output + ['']
        
        def team_2_info(self):
            output: list[str] = []

            for i in self.team_2:
                output.extend(i.display_health())
            return output + ['']
        

    class State:
        PAUSE = 0
        USER_CREATE = 1
        IDLE = 2
        SHOP = 3
        INVENTORY = 4
        FIGHT = 5
        BATTLE = 6
        BATTLEING = 7
        LEVEL_UP = 8
        DUNGEON = 10

    uid = -1
    def uid_increment():
        Game.uid +=1
        return Game.uid
    
    def level_up(self):
        output: list[str] = []
        output.extend([f"You leveled up!"])

        if self.level == ( math.floor(self.level / 10) * 10 ) + 10:
            for stat in self.stat:
                stat = self.stat[stat]
                stat.upgrade_count += self.stat_max_upgrades_per_level_iteration

        self.states.append()


        return output



    def battle_iterate(self):
        output: list[str] = []
        self.states.append(Game.State.BATTLEING)

        output.extend([f' < -------- > You Enter Battle! < -------- >', ''])

        battle = Game.Fight([self], [random.choice(Game.enemies).clone(), random.choice(Game.enemies).clone()])
        self.fight_id = battle.id
        Game.battles.append(battle)

        if self in battle.team_1:
            output.extend(battle.team_1_info())
            output.extend([f'- VS -', ''])
            output.extend(battle.team_2_info())
        else:
            output.extend(battle.team_2_info())
            output.extend([f'- VS -'])
            output.extend(battle.team_1_info())



        output.extend(Game.state_info(self, []))
        return output

    def dungeon_iterate(self):
        output: list[str] = []
        #if 1 in self.inv:
        if item.Key in self.inv:
            output.extend([f'Please select dungeon type:', f'Random Dungeon (R) | CO-OP Dungeon (M) | Exit (X)'])
            self.states.append(Game.State.DUNGEON)

        else:
            output.extend(Game.state_info(self, [f'You need a Dungeon key to proceed!']))


        return output


    def inventory_iterate(self):
        output: list[str] = [f'{self.name}\'s inventory: {self.get_inventory_space([item.ItemTypes.ITEM, item.ItemTypes.CONSUMABLE])}/{self.item_space}']
        self.states.append(Game.State.INVENTORY)

        num: int = 0
        output.extend([f'Items:'])
        if self.currency > 0:
            num += 1
            output.extend([f'{num}. Diamonds (x{self.currency})'])
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

        output.extend([f'Please select battle type:' f'Random Encounter (R) | Matchmaking (M) | Exit (X)'])

        return output
    
    def shop_state(self, cmd) -> list[str]: # Shop state
        output: list[str] = []
        num: list[str] = []
        cnt: int = 0
        shop = Game.shop

        for i in shop.items:
            cnt+=1
            num.append(str(cnt))

        if cmd in num:
            the_item = shop.items[int(cmd)-1]
            price: int = int(the_item.price * shop.price_mult)
            if self.currency >= price:  
                self.collect_item(the_item)
                output.extend(Game.state_info(self, ['', f'You bought {the_item.display()}']))
                self.currency -= price
            else:
                output.extend(Game.state_info(self, ['', f'You do not have enough Diamonds to buy this item!']))

            return output

        if cmd == 'x':
            self.states.pop(-1) # Goes back to the previous state
            output.extend(Game.state_info(self, [f'You left the shop...']))
        else:
            output.extend(Game.state_info(self, ['', f'Please enter a vaild option']))

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
            output.extend(Game.state_info(self, [f'Please enter a valid option...'])) 

        #output.extend(Game.state_info(self, []))
        return output

    def inventory_state(self, cmd) -> list[str]:
        output: list[str] = []

        num: int = 0
        count: list[str] = []
        items: list = []
        for i in self.inv:
            if i.type == item.ItemTypes.CONSUMABLE:
                num += 1
                count.append(str(num))
                items.append(i)


        if cmd in count:
            output.extend(Game.state_info(self, items[int(cmd)-1].use_item(self, self.inv)))
            items.clear
        elif cmd == 'x':
            self.states.pop(-1) # Goes back to the previous state
            output.extend(Game.state_info(self, [f'You closed your inventory...']))
        else:
            output.extend(Game.state_info(self, ['', f'Please enter a valid option...']))

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

        if cmd == 'r':
            output += Game.battle_iterate(self)
        elif cmd == 'x':
            self.states.pop(-1)
            output.extend(Game.state_info(self, [f'You stopped searching for a fight']))
        else:
            output.extend(Game.state_info(self, ['', f'Please enter a vaild option']))

        return output
    
    def battle_state(self, cmd) -> list[str]:
        output: list[str] = []

        if cmd == '':
            pass
        else:
            output.extend(Game.state_info(self, ['', f'Please enter a valid option']))

        return output

    def iterate(player, cmd) -> list[str]:
        output: list[str] = []
        state = player.states[-1]
        cmd = str(cmd).lower()

        if cmd == 'l1':
            player.level += 1
        elif cmd == 'l10':
            player.level += 10

        else:        
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
            elif state == Game.State.BATTLEING:
                output.extend(Game.battle_state(player, cmd))
            else:
                #self.states.append(Game.State.IDLE)
                output += [f'{cmd} what? how did you get here.']
        
        return output
    
    def state_info(self, current_state_leave_message: list[str]) -> list[str]:
        output: list[str] = []
        state = self.states[-1]

        if state == Game.State.IDLE:
            output.extend([f'What to you want to do now?', f'Shop (S) | Fight (F) | Dungeon (D) | Stats (T) | Inventory (I)', ''])
        elif state == Game.State.DUNGEON:
            output.extend([f'Please select dungeon type:' f'Random Dungeon (R) | CO-OP Dungeon (M) | Exit (X)'])
        elif state == Game.State.BATTLEING:
            output.extend([f'What to you want to do now?', f'Attack (A) | Inventory (I) | '])
        elif state == Game.State.INVENTORY:
            output.extend(Game.inventory_iterate(self))
            self.states.pop(-1)
        elif state == Game.State.SHOP:
            output.extend(Game.shop_iterate(self))
            self.states.pop(-1)

        output.extend(current_state_leave_message)
        return output
        

# ///////////////////////
if __name__ =='__main__':

    while True:
        print(Game.iterate('player', input("Command?")))
