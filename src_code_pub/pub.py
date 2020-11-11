class Pub: 

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock = stock

    def sell_drink(self, customer, drink):
        # Money leaves customer wallet
        # Increase money in pub till by drink price
        if customer.age > 18 and customer.drunkenness < 10:
            self.till += drink.price
            customer.wallet -= drink.price
            customer.increase_drunkenness(drink)

    def sell_food(self, customer, food):
        self.till += food.price
        customer.wallet -= food.price
        customer.decrease_drunkenness(food)

    # def stock_value(self):
    #     total_values_by_drink = []
    #     for drink_for_sale in self.stock:
    #     total_values_by_drink.append(drink_for_sale.amount * drink_for_sale.drink.price)
