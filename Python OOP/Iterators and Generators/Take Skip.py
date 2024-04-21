
class take_skip:
    def __init__(self, step:int, count:int) -> None:
        self.step = step
        self.count = count
        self.it = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.it == self.count-1:
            raise StopIteration
        
        self.it+=1
        
        return self.it*self.step

        
numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print()    
numbers = take_skip(10, 5)
for number in numbers:
    print(number)	


        