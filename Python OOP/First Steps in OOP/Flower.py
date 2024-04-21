class Flower:
    is_happy = False
    
    def __init__(self, nm:str, w_r:int):
        self.name = nm
        self.water_requirements = w_r
        
    def water(self, quantity:int)->bool:
        if quantity>=self.water_requirements:
            self.is_happy = True
        else:
            self.is_happy = False
            
    def status(self)->str:
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"
        
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

print(flower.is_happy) #True
print(Flower.is_happy) #False
