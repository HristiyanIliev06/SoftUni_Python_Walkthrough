from project.food.food import Food

class Dessert(Food):
    def __init__(self, n: str, p: float, grams: float, cals: float) -> None:
        super().__init__(n, p, grams)
        self.__calories = cals
        
    @property
    def calories(self):
        return self.__calories
    
