#
#   account class
#   account.py
#

class Global:
    uid = -1
    def assign_uid() -> int:
        Global.uid += 1
        return Global.uid
    
    chat = []



class Account:
    def __init__(self, player) -> None:

        self.uid = Global.assign_uid()
        self.player = player.name
        self.input = ''

    def print_info(self):
        info_out = f"Username: {self.player}\nUID: {self.uid}"

        return info_out
