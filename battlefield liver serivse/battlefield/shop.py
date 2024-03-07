#
##

class Shop:
    def __init__(self, shop_name, items, price_mult) -> None:

        self.name = shop_name
        self.items = items
        self.price_mult = price_mult

    def buy(self, buyer):

        num = 0
        item_count = []
        if len(self.items) > 0:

            user_input = ''
            while not user_input == 'x':
                for item in self.items:
                    num += 1
                    item_count.append(str(num))

                    print(f'{num}. {item.name}')
                
                user_input = input(f'\nWhat would you like to buy? ').lower()
                if str(user_input) in item_count:

                    price = item.price*self.price_mult

                    if not price > buyer.currency:
                        buyer.currency -= price
                        buyer.collect_item(self.items[user_input])
        else:
            print(f'The {self.name} is empty! Come back later ...')
