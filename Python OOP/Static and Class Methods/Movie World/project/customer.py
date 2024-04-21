#from dvd import DVD

class Customer():
    
    def __init__(self, name:str, age:int, id:int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []
        
    def __repr__(self):
        rented_dvds_names = []
        for rd in self.rented_dvds:
            rented_dvds_names.append(rd.name)
            
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join( rented_dvds_names)})"
    