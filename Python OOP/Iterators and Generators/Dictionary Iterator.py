class dictionary_iter:
    def __init__(self, dictionary:dict) -> None:
        self.dictionary = dictionary
        self.it = -1
        self.items = iter(dictionary.items())
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.it==len(self.dictionary)-1:
            raise StopIteration
         
        self.it +=1
        
        return next(self.items)
    
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
    
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)	

