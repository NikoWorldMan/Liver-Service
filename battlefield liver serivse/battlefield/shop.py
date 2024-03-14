#
##

class Shop:
    def __init__(self, shop_name: str, price_mult: float, items: list) -> None:

        self.name = shop_name
        self.items = items
        self.price_mult = price_mult
