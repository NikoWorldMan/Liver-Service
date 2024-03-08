
from battlefield.player import classes

def action_loop():
    while True:
        print(f'\n')
        print(f'Select one of the following actions:\nShop: (S) | Fight: (F) | Dungeon: (D) | Inventory: (I) | Armory: (A) ')
        user_input = input('What would you like to do now? ').lower()

        if user_input == 'i':
            print("item")

        elif user_input == 'f':
            print("fight")

        elif user_input == 's':
            print("shop")

        elif user_input == 'a':
            print("armory")

        elif user_input == 'd':
            print("dungeon")

def lvl_up():
    stats = 1
    print("You Leveled up!")
    print("player - Lv. 5")

    input("Choose an extra stat to upgrade:")
    print(stats)
    print()
    input(f'= ')

def start_game():

    classes = ['Mage', 'Ranger', 'Warrior']

    print("Welcome to Fightcraft!")
    name = input("Choose your name: ").upper()
    print("Welcome!", name)
    print()
    print("Choose your class: ")


    count = 0
    num = []
    for i in player.classes:
        count +=1
        num.append(str(count))

        print(f'{count}. {i.type} - {i.desc}')

    print("\n =")

start_game()
