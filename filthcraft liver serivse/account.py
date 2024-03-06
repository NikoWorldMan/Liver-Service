#
#   account class
#   account.py
#
print()

import time
import copy
import random

class Global:
    uid = 80000

def uid_increment(self):
    self.uid = Global.uid
    Global.uid += 1



class Account:
    def __init__(self, player, password) -> None:
        self.uid = 0
        self.player = player
        self.password = password

    def clone(self):
        uid_increment(self)
        return copy.deepcopy(self)
    
    def print_info(self):
        print(f"Username: {self.player}")
        print(f"Password: {self.password}")
        print(f"UUID: {self.uid}")
        print()


classes = ["Mage", "Summoner", "Warrior", "Ranger", "Necromancer"]
users = []


for i in range(0, 100080):
    users.append(Account(random.choice(classes), random.randrange(1,99)).clone())

time.sleep(0.007)

print()
for user in users:
    print("Created account:")
    user.print_info()

    time.sleep(0.007)

Account(random.choice(classes), random.randrange(1,99)).clone()