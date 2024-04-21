class sequence_repeat:
    def __init__(self, sequence:str, number:int) -> None:
        self.sequence = sequence
        self.number = number
        self.it = -1
        
    def  __iter__(self):
        return self
    
    def __next__(self):
        if self.number==0:
            raise StopIteration
        
        if self.it==len(self.sequence)-1:
            self.it=-1
        
        self.number-=1        
        self.it+=1
        return self.sequence[self.it]
    
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
    
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

       