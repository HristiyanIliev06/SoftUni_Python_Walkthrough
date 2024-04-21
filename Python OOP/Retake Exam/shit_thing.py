from abc import abstractmethod, ABC

class BaseClient(ABC):
    ALLOWED_TYPES = ['RegularClient', 'VIPClient']
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value:str):
        if value.strip()=='':
            raise ValueError("Client name should be determined!")
        
        self.__name = value
        
    @property
    def membership_type(self):
        return self.__membership_type
    
    @membership_type.setter
    def membership_type(self, value:str):
        if value not in self.ALLOWED_TYPES:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass
    
    def apply_discount(self):
        discount_percentage = 0
        if self.points>=100:
            discount_percentage = 10        
        elif 50<=self.points<100:
            discount_percentage = 5
        
        self.points -= int(discount_percentage*10)
        return (discount_percentage, self.points)



class RegularClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, 'RegularClient')
        
    def earning_points(self, order_amount: float)->int:
        earned_points = order_amount//10
        self.points+=earned_points
        
        return earned_points
    

class VIPClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, 'VIPClient')
        
    def earning_points(self, order_amount: float)->int:
        earned_points = order_amount//5
        self.points+=earned_points
        
        return earned_points
    
from abc import ABC, abstractmethod

class BaseWaiter(ABC):
    def __init__(self, name: str, hours_worked: int):
        self.name = name
        self.hours_worked = hours_worked
        
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value:str):
        if len(value)>50 or len(value) < 3:
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")
        self.__name = value 
        
    @property
    def hours_worked(self):
        return self.__hours_worked
    
    @hours_worked.setter
    def hours_worked(self, value:int):
        if value<0:
            raise ValueError("Cannot have negative hours worked!")
        
        self.__hours_worked = value
        
    @abstractmethod
    def calculate_earnings(self)->float:
        pass
    
    @abstractmethod
    def report_shift(self)->str:
        pass
    
    def __str__(self):
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}"   
    
class FullTimeWaiter(BaseWaiter):
    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)
        
    def calculate_earnings(self)->float:
        return self.hours_worked*15.0
    
    def report_shift(self)->str:
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."   
    
class HalfTimeWaiter(BaseWaiter):
    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)
        
    def calculate_earnings(self)->float:
        return self.hours_worked*12.0
    
    def report_shift(self)->str:
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
    
from typing import List

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
            return f"{client_name} received a {int(discount_percentage)}% discount. Remaining points {int(remaining_points)}"
        
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
    
# Create an instance of SphereRestaurantApp
sphere_restaurant_app = SphereRestaurantApp()

# Hire some waiters
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))

# Admit some clients
print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))

# Process shifts
print(sphere_restaurant_app.process_shifts("John"))
print(sphere_restaurant_app.process_shifts("Alice"))
print(sphere_restaurant_app.process_shifts("Emily"))
print(sphere_restaurant_app.process_shifts("Frank"))

# Process client orders
print(sphere_restaurant_app.process_client_order("Bob", 100.0))
print(sphere_restaurant_app.process_client_order("Eve", 500.0))
print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
print(sphere_restaurant_app.process_client_order("Bob", 750.0))
print(sphere_restaurant_app.process_client_order("Lila", 550.0))
print(sphere_restaurant_app.process_client_order("Oscar", 84.0))

# Apply discounts to clients
print(sphere_restaurant_app.apply_discount_to_client("Lila"))
print(sphere_restaurant_app.apply_discount_to_client("Eve"))
print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
print(sphere_restaurant_app.apply_discount_to_client("Bob"))

# Generate report
print(sphere_restaurant_app.generate_report())
