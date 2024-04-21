def grocery_store(**kwargs):
    lengths_of_names = []
    checker = 0
    sorting = []
    
    for k, v in kwargs.items():
        if v in kwargs.values():
            lengths_of_names.append(len(k))
            
    for length in lengths_of_names:
        if checker!=length: checker=length
        else:
            sorting = sorted(kwargs.items(), key=lambda name: name[0])
            
    sorted(kwargs.items(), key=lambda name: -len(name[0]))

        
            
                
        


print(grocery_store(bread=5,
    pasta=12,
    eggs=12,
))