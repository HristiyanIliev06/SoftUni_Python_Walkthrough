class Product:
    def __init__(self, n:str, p:float) -> None:
        self.__name = n
        self.__price = p
        
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
