#
#   account class
#   account.py
#
print()

import time
import copy
import random

class Global:
    uid = -1
    def assign_uid():
        Global.uid += 1
        return Global.uid


class Account:
    def __init__(self, player) -> None:

        self.uid = Global.assign_uid()
        self.player = player

    def print_info(self):
        info_out = f"Username: {self.player}\nPassword: rg"

        return info_out
