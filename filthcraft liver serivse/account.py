#
#   account class
#   account.py
#

import copy

class Account:
    def __init__(self) -> None:
        pass

    username = "user"
    password = 1

    def clone(self):
        return copy.deepcopy(self)
    
    def print_info(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")


user = Account()

user_1 = user.clone()

user_2 = user.clone()

user_2.password = 6
user_2.username = "wow"

user_1.print_info()
user_2.print_info()