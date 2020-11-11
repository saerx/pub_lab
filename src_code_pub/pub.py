class Pub: 

    def __init__(self, name, till):
        self.name = name
        self.till = till
        # self.drinks = drinks

    def sell_drink(self, customer, drink):
        # Money leaves customer wallet
        # Increase money in pub till by drink price
        if customer.age > 18 and customer.drunkenness < 10:
            self.till += drink.price
            customer.wallet -= drink.price
            customer.increase_drunkenness(drink)

        

