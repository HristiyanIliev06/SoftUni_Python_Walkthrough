def age_assignment(*args, **kwargs):
    dictionary = {}
    result = []
    
    for  k, v in kwargs.items():
        for arg in args:
            if k in arg:
                dictionary[arg] = v
                break
            
    dictionary = sorted(dictionary.items(), key=lambda l: l[0])
    for tuple in dictionary:
      result.append(f"{tuple[0]} is {tuple[1]} years old.")
    
    return '\n'.join(result)  
                
    
    
print(age_assignment("Deyan","Radiana","Hristiyan", H=17, D=50, R=49)) 