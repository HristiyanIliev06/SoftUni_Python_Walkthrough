def cookbook(*args): #0/100 ;( Pov: да си жертва на обстоятелствата(недостиг на време))
    book = {}
    
    for recipe_name, cuisine, ingredients in args:
        
        if cuisine not in book.keys():
            book[cuisine] = {}
        book[cuisine][recipe_name] = ingredients
        
        book = sorted(book.keys(), key=lambda a: a[0])
        
        
        
    book = dict(sorted(book.items(), key=lambda x: (-len(x[1]), (x[0]))))
    
    result = ''
    for k, v in book.items():   
        result+=f"{k} cuisine contains {len(v)} recipes:\n"
        for k1, v1 in v.items():
            result+=f"  *{k1} -> Ingredients: {', '.join(v1)}\n"
        
    return result.strip()

def cookbookfromdiscord(*recipes): #working!
    cuisine_count = {}
    cuisine_recipes = {}
    for i in range(len(recipes)):
        recipe_name, cuisine, ingredients = recipes[i]
        if cuisine not in cuisine_count:
            cuisine_count[cuisine] = 1
            cuisine_recipes[cuisine] = [(recipe_name, ingredients)]
        else:
            cuisine_count[cuisine] += 1
            cuisine_recipes[cuisine].append((recipe_name, ingredients))
 
    sorted_cuisine_count = sorted(cuisine_count.items(), key=lambda x: (-x[1], x[0]))
    result = ""
    for key, value in sorted_cuisine_count:
        result += f"{key} cuisine contains {value} recipes:\n"
        for k, v in sorted(cuisine_recipes[key], key=lambda x: x[0]):
            result += f"  * {k} -> Ingredients: {', '.join(v)}\n"
 
    return result
    


print(cookbookfromdiscord(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))    