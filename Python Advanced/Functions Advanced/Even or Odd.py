def even_odd(*args):
    if args[-1]=='even':
        result = list(filter(lambda a: a%2==0, args[:-1]))
        return result
    else:  
        result = list(filter(lambda a: a%2!=0, args[:-1]))
        return result
    
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))