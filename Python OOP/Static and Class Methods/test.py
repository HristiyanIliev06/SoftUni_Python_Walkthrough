class Customer():
    
    def __init__(self, name:str, age:int, id:int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []
        
    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join( self.rented_dvds)})"


customers = []    
c1 = Customer("John", 16, 1)
customers.append(c1)
c2 = Customer("Anna", 55, 2)
customers.append(c2)

for customer in customers:
    if customer.age==55:
        c = customer
        
print(c.__repr__())