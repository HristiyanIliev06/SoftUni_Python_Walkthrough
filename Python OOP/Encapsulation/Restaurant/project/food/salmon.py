from project.food.main_dish import MainDish

class Salmon(MainDish):
    def __init__(self, n: str, p: float) -> None:
        super().__init__(n, p, 22)