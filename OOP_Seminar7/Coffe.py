from Product import Product


class Coffe(Product):
    price = 0

    def __init__(self, name, volume, price) -> None:
        super().__init__(name, volume)
        self.price = price

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price = price