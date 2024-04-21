from project.food.starter import Starter

class Soup(Starter):
    def __init__(self, n: str, p: float, grams: float) -> None:
        super().__init__(n, p, grams)