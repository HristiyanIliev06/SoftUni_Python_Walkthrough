from project.product import Product

class Beverage(Product):
    def __init__(self, n: str, p: float, ml:float) -> None:
        super().__init__(n, p)
        self.__milliliters = ml
     
    @property   
    def milliliters(self):
        return self.__milliliters
    
beverage = Beverage("tea", 2, 250)