class Worker:
    
    def __init__(self, n, a, s) -> None:
        self.name = n
        self.age = a
        self.salary = s
        
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"