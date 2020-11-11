class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
        

    # def decrease_drunkenness(self, food):
    #     self.drunkenness -= food.rejuvenation_level