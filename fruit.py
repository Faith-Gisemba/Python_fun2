class Fruit:
    taste="sweet"
    def __init__(self,colour,name,price):
        self.colour = colour
        self.name=name
        self.price=price
    def buy_fruits(self):
        return f"I bought 10 fruits at the price of {self.price}ksh"
    def make_juice(self):
        return f"I made {self.taste} {self.name} juice"
    def sell_juice(self):
        return f"I sold {self.taste} {self.name} juice at a price of {self.price}ksh per glass"