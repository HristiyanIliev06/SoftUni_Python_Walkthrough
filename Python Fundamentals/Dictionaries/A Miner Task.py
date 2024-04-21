inventory = {}
count_of_times = 0
key = None
old = 0

while True:
    info = input()
    if info=="stop": break
    
    count_of_times+=1
    if count_of_times%2>0: 
        key = info
    if count_of_times%2==0:
        if key in inventory.keys():
            old = int(inventory[key])+int(info)
            inventory[key] = old
        else: inventory[key] = info
        key = None
        
for item in inventory:
    print(f"{item} -> {inventory[item]}")