class DVD:
       
    def __init__(self, n:str, id:int, c_y:int, c_m:str, age_restriction:int) -> None:
        self.name = n
        self.id = id
        self.creation_year = c_y
        self.creation_month = c_m
        self.age_restriction = age_restriction
        self.is_rented = False
    
     
    @classmethod   
    def from_date(cls, id:int, name:str, date:str, age_restriction:int):
        months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        day_month_year = date.split('.')
        return cls(name, id, int(day_month_year[2]), months[int(day_month_year[1])-1] , age_restriction)
    
    def __repr__(self):
        status = ""
        
        if self.is_rented: status = 'rented'
        else: status = 'not rented'
        
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"