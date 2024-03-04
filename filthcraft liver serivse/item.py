class Main:
    def __init__(self, size) -> None:
        
        self.size = size

    def collect(self, collecter):

        collecter.inv.append(self)

class Resource(Main):
    def __init__(self) -> None:
        super().__init__()

    def collect(self, collecter):
        collecter.self += self.size

class Item(Main):
    def __init__(self) -> None:
        super().__init__()

