#
#   account class
#   account.py
#

from battlefield.player import SetClasses
import battlefield.player as player
from battlefield.player import Player

class States:
    PLAYER = 0
    NAME = 1

class Account:
    def __init__(self, uid: int) -> None:

        self.uid = uid
        self.player: Player = None
        self.name = None
        self.input = ''
        self.state = None

        self.texty = ['Welcome, new player!', '']
        self.texty.extend(self.choose_player_class_iteration(''))

    def assign_player(self, player):
        self.player = player

    def print_info(self):
        info_out = f"User with UID: {self.uid}"

        return info_out
    
    def despawn(self, *args: str):
        Global.accounts.remove(self)
        print(f"Deteted account with UID: {self.uid}")
        for i in args:
            print(f'Reason(s):\n{i}')
        self = None

    def set_name(self, name: str) -> list[str]:
        output: list[str] = []

        if self.state == States.NAME:

            self.name = name.upper()
            self.player.name = self.name
            output.extend([f'Welcome to battlefields, {name}!', ''])
        else:
            self.state = States.NAME

            output.extend(['', f'Name your character...'])
        return output    

    def choose_player_class_iteration(self, cmd):
        output: list[str] = []

        if self.state == States.PLAYER:
            output += self.choose_player_class(cmd)
        else:
            self.state = States.PLAYER

            output.extend([f'Please choose your class', f'1. Templar', f'2. Mage', f'3. Psion', f'4. Necromancer'])
        return output

    def choose_player_class(self, cmd: str) -> list[str]:
        output: list[str] = []
        cmd.lower()

        if cmd == '1':
            self.player = SetClasses.templar()
            output.extend([f'You are now a {player.Templar.type}!'])

        elif cmd == '2':
            self.player = SetClasses.mage()
            output.extend([f'You are now a {player.Blightbringer.type}!'])

        elif cmd == '3':
            self.player = SetClasses.psion()
            output.extend([f'You are now a {player.Psion.type}!'])

        elif cmd == '4':
            self.player = SetClasses.necromancer()
            output.extend([f'You are now a {player.Necromancer.type}!'])
    
        else:
            output.extend([f'Please enter a valid option...'])
        return output


class Global:
    uid = -1
    def assign_uid() -> int:
        Global.uid += 1
        return Global.uid
    
    chat: list[str] = []

    accounts: list[Account] = []

    def create_account(uid: int | None):
        if uid == None:
            uid = Global.assign_uid()

        new_account = Account(uid)

        Global.accounts.append(new_account)
        print(f"Created Account with UID: {uid}")
    