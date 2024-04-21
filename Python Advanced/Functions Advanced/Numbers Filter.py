def even_odd_filter(**kwargs):
    dictionary = {}
    result = {}
    
    for k, v in kwargs.items():
        if k == "odd":
            filtered = list(filter(lambda x: x%2!=0, v))
            dictionary[k] = filtered
        else: 
            filtered = list(filter(lambda x: x%2==0, v))
            dictionary[k] = filtered
    
    done = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple in done:
        result[tuple[0]] = tuple[1]
        
    return result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
