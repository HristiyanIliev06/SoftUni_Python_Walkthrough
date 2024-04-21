text = input()

ordered = []
for char in text:
    ordered.append(char)
ordered.sort()

set_of_items = set([])
result = {}

for item in ordered:
    if set_of_items.issuperset(set(item)) == False:
        set_of_items.add(item)
        occurances = text.count(item)
        result[item] = occurances
     
for k,v in result.items():
    print(f'{k}: {v} time/s')
        
