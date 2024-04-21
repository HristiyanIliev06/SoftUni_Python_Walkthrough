from project.beverage.beverage import Beverage

class HotBeverage(Beverage):
    def __init__(self, n: str, p: float, ml: float) -> None:
        super().__init__(n, p, ml)