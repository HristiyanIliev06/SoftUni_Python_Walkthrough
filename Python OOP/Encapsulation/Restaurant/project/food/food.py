from project.product import Product

class Food(Product):
    def __init__(self, n: str, p: float, grams:float) -> None:
        super().__init__(n, p)
        self.__grams= grams
     
    @property   
    def grams(self):
        return self.__grams