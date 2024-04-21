from project.food.dessert import Dessert

class Cake(Dessert):
    def __init__(self, n: str) -> None:
        super().__init__(n, 5, 250, 1000)