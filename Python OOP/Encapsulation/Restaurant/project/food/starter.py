from project.food.food import Food

class Starter(Food):
    def __init__(self, n: str, p: float, grams: float) -> None:
        super().__init__(n, p, grams)