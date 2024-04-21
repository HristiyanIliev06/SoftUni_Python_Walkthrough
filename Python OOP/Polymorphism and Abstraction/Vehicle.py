from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity:float, fuel_consumption:float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        
    @abstractmethod
    def drive(self, distance:float):
        fuel_expense = self.fuel_consumption*distance
        
        if fuel_expense<=self.fuel_quantity:
            self.fuel_quantity-=fuel_expense
    
    @abstractmethod        
    def refuel(self, fuel:float):
        self.fuel_quantity+=fuel
        
class Car(Vehicle):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption + 0.9)
        
    def drive(self, distance: float):
        super().drive(distance)
    
    def refuel(self, fuel: float):
        super().refuel(fuel)
    
class Truck(Vehicle):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption+1.6)
        
    def drive(self, distance: float):
        super().drive(distance)
    
    def refuel(self, fuel: float):
        super().refuel(0.95*fuel)
    
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
