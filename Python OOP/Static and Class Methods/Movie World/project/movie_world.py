from project.dvd import DVD
from project.customer import Customer

class MovieWorld:
    def __init__(self, name:str) -> None:
        self.name = name
        self.customers = []
        self.dvds = []
    
    @staticmethod    
    def dvd_capacity():
        return 15
    
    @staticmethod
    def customer_capacity():
        return 10
    
    def add_customer(self, customer:Customer):
        if len(self.customers)<self.customer_capacity():
            self.customers.append(customer)
            
    def add_dvd(self, dvd: DVD):
        if len(self.dvds)<self.dvd_capacity():
            self.dvds.append(dvd)
            
    def rent_dvd(self, customer_id:int, dvd_id:int):
        
        for dvd in self.dvds:
            if dvd_id == dvd.id:
                rdvd = dvd
                break
                
        for customer in self.customers:
            if customer_id == customer.id:
                rcustomer = customer
                break
                
        for crd in rcustomer.rented_dvds:    
            if rdvd.name==crd.name:
                return f"{rcustomer.name} has already rented {rdvd.name}"
            
        if rdvd.is_rented:
            return "DVD is already rented"
        elif rcustomer.age<rdvd.age_restriction:
            return f"{rcustomer.name} should be at least {rdvd.age_restriction} to rent this movie"
        
        
        dvd.is_rented = True        
        rcustomer.rented_dvds.append(rdvd)                   
        return f"{rcustomer.name} has successfully rented {rdvd.name}"
                
    def return_dvd(self, customer_id, dvd_id):
             
        for dvd in self.dvds:
            if dvd_id == dvd.id:
                rdvd = dvd
                break
                
        for customer in self.customers:
            if customer_id == customer.id:
                rcustomer = customer
                break
        
        for crd in rcustomer.rented_dvds:    
            if rdvd.name==crd.name:
                rcustomer.rented_dvds.remove(rdvd)
                rdvd.is_rented = False
                return f"{rcustomer.name} has successfully returned {rdvd.name}"
            
        return f"{rcustomer.name} does not have that DVD"
        
    
    def __repr__(self) -> str:
        result = []
        for customer in self.customers:
            result.append(customer.__repr__())
            
        for dvd in self.dvds:
            result.append(dvd.__repr__())
            
        return '\n'.join(result)
            
c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
         
        