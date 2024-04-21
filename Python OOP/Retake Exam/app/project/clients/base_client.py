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
