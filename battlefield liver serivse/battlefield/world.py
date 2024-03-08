#
#

import random
import player
import mobs
import time
import entity

class World:
    turn_cycle = 10000


    class Shop:
        def __init__(self, contents) -> None:
            self.contents = contents

        def open_shop(self):
            pass


    def start_game():

        thePlayer = player.Player(input(f"Name your character! ").upper(), 1, 6000, 2000, 1500, 3000, 100, 10, 50, 10, 5, 10, 0, 100, None).clone()
        thePlayer.list_stats()
        input()

        while True:   # Loop

            thePlayer.options_loop()
            if action == "s":                               # If 's' is pressed
                openShop(p)                                  # Opens the Shop

            elif action == "f":                                         # If 'f' is pressed starts a fight with a random mob
                print("\n------- You Enter Battle! -------\n")
                fight(p)

                if int(random.randrange(1, 4)) == 1:
                    changeBiome(p, weighted_choices(biomesWeight))

            elif action == "i":
                print("- Items")
                displayInv(p, p.inventory, 0)
                print("\n- Consumable Items")
                displayInv(p, p.consumableInventory, 1)
            
            elif action == "x":         # if 'x' is pressed, leave the game
                print("you left ...")   # Leave game message
                exit(0)                 # Stop the game

            elif action == "t":
                playerStats(p)

            else:
                print(action,"is not an option")


    def battle_info(self):
        self.set_stats()
        self.turn_value = 100
        if "SPD" in self.stats:
            self.turn_value = self.get_action_value(World.turn_cycle)
        self.display_health()


    def battle(team_1, team_2):

        print()

        for entity in team_1:
            World.battle_info(entity)
        print(" - VS -")

        for entity in team_2:
            World.battle_info(entity)

        print()

        while len(team_1) > 0 and len(team_2) > 0:

            for entity in team_1 + team_2:
                entity.turn_value -= 1

                entity.overflow_value = 0
                while entity.turn_value <= 0:
                    time.sleep(0.4)
                    
                    entity.overflow_value = entity.turn_value

                    if entity in team_1:
                        if len(team_2) > 0:
                            print(entity.name,"attacked team 2")
                            entity.attack_options(team_2)
                    if entity in team_2:
                        if len(team_1) > 0:
                            print(entity.name,"attacked team 1")
                            entity.attack_options(team_1)

                    entity.turn_value = entity.get_action_value(World.turn_cycle)

                    print("\n-----------------\n")


                entity.turn_value += entity.overflow_value


        print("-------- The Battle Ended --------")

        print("team 1",team_1, "team 2 \n",team_2)
        print()


creep = mobs.Creeper("Crepr", 18, 3000, 500, 400, 14, 0, 0, 4)

zomb = mobs.Zombie("Zmbie", 17, 5000, 600, 400, 7, 60, 120)

the_player= player.Player("Sturl", 20, 5000, 200, 90, 1000, 9, 100, 400, 10, 10, 10, 0, 100)

World.battle([zomb.clone()], [creep.clone()])
