from Product import Product


class Tea(Product):
    temperature = 0

    def __init__(self, name, volume, temperature) -> None:
        super().__init__(name, volume)
        self.temperature = temperature

    def getTemperature(self):
        return self.temperature

    def setTemperature(self, temperature):
        self.temperature = temperature