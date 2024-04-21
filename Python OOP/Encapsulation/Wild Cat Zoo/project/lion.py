from project.animal import Animal

class Lion(Animal):
    
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 50)
        
        
        def __repr__():
            super().__repr__()
            
'''lion = Lion("Simba", "male", 12)
print(lion.__repr__())'''