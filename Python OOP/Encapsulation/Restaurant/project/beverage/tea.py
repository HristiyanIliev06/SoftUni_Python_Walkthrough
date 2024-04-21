from project.beverage.hot_beverage import HotBeverage

class Tea(HotBeverage):
    def __init__(self, n: str, p: float, ml: float) -> None:
        super().__init__(n, p, ml)
        
tea =Tea("Alp", 3, 250)
        