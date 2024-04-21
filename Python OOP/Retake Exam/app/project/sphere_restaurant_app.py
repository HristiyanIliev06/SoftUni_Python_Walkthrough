from typing import List

from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter

class SphereRestaurantApp:
    CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}
    WAITER_TYPES = {"HalfTimeWaiter": HalfTimeWaiter, "FullTimeWaiter": FullTimeWaiter}
    
    def __init__(self):
        self.waiters:List[HalfTimeWaiter|FullTimeWaiter] = []
        self.clients:List[RegularClient|VIPClient] = []
        
    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITER_TYPES.keys():
            return f"{waiter_type} is not a recognized waiter type."
        
        if self._get_waiter(waiter_name)!=None:
            return f"{waiter_name} is already on the staff."
        
        waiter = self.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append((waiter))
        return f"{waiter_name} is successfully hired as a {waiter_type}."
        
    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES.keys():
            return f"{client_type} is not a recognized client type."
        
        if self._get_client(client_name)!=None:
            return f"{client_name} is already a client."
        
        client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append((client))
        return f"{client_name} is successfully admitted as a {client_type}."
        
    def process_shifts(self, waiter_name: str):
        waiter = self._get_waiter(waiter_name)
        if waiter!=None:
            return waiter.report_shift()
        
        return f"No waiter found with the name {waiter_name}."
    
    def process_client_order(self, client_name: str, order_amount: float):
        client = self._get_client(client_name)
        if client!=None:
            return f"{client_name} earned {int(client.earning_points(order_amount))} points from the order."
        
        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        client = self._get_client(client_name)
        if client!=None:
            discount_percentage, remaining_points = client.apply_discount()
            return f"{client_name} received a {int(discount_percentage)}% discount. Remaining points {remaining_points}"
        
        return f"{client_name} cannot get a discount because this client is not admitted!"

    
    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: (-w.calculate_earnings(), w.name))        
        total_earnings = sum([w.calculate_earnings() for w in sorted_waiters])
        total_client_points = int(sum([c.points for c in self.clients]))
        clients_count = len(self.clients)
        
        result = ['$$ Monthly Report $$',
        f'Total Earnings: ${total_earnings:.2f}',
        f'Total Clients Unused Points: {total_client_points}',
        f'Total Clients Count: {clients_count}', '** Waiter Details **'
            ]
        
        waiters_details = '\n'.join(str(sw) for sw in sorted_waiters)
        result.append(waiters_details)
        
        return '\n'.join(result)

    
    # Helper methods
    def _get_client(self, client_name: str):
        clients = [c for c in self.clients if c.name == client_name]
        return clients[0] if clients else None

    def _get_waiter(self, waiter_name: str):
        waiters = [w for w in self.waiters if w.name == waiter_name]
        return waiters[0] if waiters else None