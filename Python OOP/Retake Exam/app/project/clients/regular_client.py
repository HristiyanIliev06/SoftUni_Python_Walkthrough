from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, 'RegularClient')
        
    def earning_points(self, order_amount: float)->int:
        earned_points = order_amount//10
        self.points+=earned_points
        
        return earned_points