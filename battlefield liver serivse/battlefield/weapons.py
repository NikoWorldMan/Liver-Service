#
#
#

class Weapon:
    def __init__(self) -> None:
        pass

    def basic(self):
        ...

class Templar(Weapon):
    def __init__(self) -> None:
        super().__init__()