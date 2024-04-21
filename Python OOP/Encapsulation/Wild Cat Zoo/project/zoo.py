from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet

class Zoo:
    
    animals = []
    workers = []
    
    def __init__(self, n:str, b:int, ac:int, wc:int):
        self.name = n
        self.__budget = b
        self.__animal_capacity = ac
        self.__workers_capacity = wc
        
        
        
    def add_animal(self, animal:object, price:int):
        
        if self.__animal_capacity==len(self.animals):
            return "Not enough space for animal"
        
        if self.__budget<=0:
            return "Not enough budget"
        
        self.animals.append(animal)
        self.__budget-=price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        
    def hire_worker(self, worker:object):
        if len(self.workers)==self.__workers_capacity:
            return "Not enough space for worker"
        else:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
            
    def fire_worker(self, name:str):
        names = [worker.name for worker in self.workers]
            
        if name in names:
            return f"{name} fired successfully"
        else:
            return f"There is no {name} in the zoo"
        
    def pay_workers(self):
        sum = 0
        
        for worker in self.workers:
            sum+=worker.salary
        
        if sum<=self.__budget:
            self.__budget-=sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"
        
    def tend_animals(self):
        sum = 0
        
        for animal in self.animals:
            sum+=animal.money_for_care
            
        if sum<=self.__budget:
            self.__budget-=sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."
        
    def profit(self, amount:int):
        self.__budget+=amount
        
    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        
        for animal in self.animals:
           if type(animal) == Cheetah:
               cheetahs.append(animal)
           elif type(animal) == Lion:
               lions.append(animal)
           else:
               tigers.append(animal)
           
        print(f"You have {len(self.animals)} animals:")
        
        print(f"----- {len(lions)} Lions:")    
        [print(lion.__repr__()) for  lion in lions]
        
        print(f"----- {len(tigers)} Tigers:")    
        [print(tiger.__repr__()) for  tiger in tigers]
        
        print(f"----- {len(cheetahs)} Cheetahs:")    
        [print(cheetahs[i].__repr__()) for i in range(len(cheetahs) - 1 )]
        return cheetahs[-1].__repr__()
        
    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        
        
        for worker in self.workers:
            if type(worker) == Keeper:
                keepers.append(worker)
            elif type(worker) == Caretaker:
                caretakers.append(worker)
            else:
                vets.append(worker)
           
        print(f"You have {len(self.workers)} workers:")
        
        print(f"----- {len(keepers)} Keepers:")    
        [print(keeper.__repr__()) for  keeper in keepers]
        
        print(f"----- {len(caretakers)} Keepers:")    
        [print(caretaker.__repr__()) for  caretaker in caretakers]
        
        print(f"----- {len(vets)} Vets:")    
        [print(vets[i].__repr__()) for i in range(len(vets) - 1 )]
        return vets[-1].__repr__()
        

'''zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())'''

        