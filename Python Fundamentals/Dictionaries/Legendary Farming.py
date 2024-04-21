inventory = {}
key = ""
value = 0 #НЕ ПРАВИЛНА!!!

while True:
    farming = input().split()
    for i in range(len(farming)):
        shift = 0
        if i%2==0:
            value = int(farming[i])
        else:
            key = farming[i].lower()
            shift+=1
        if shift!=0 and key not in inventory.keys(): inventory[key] = value
        elif shift!=0 and key in inventory.keys():
            value+=int(farming[i-1])
            inventory[key] = value
    for k, v in inventory.items():
        if k=='shards' and v>=250:
            inventory[k]-=250
            print(f"Shadowmourne obtained!")
            print(f"{k}: {v}")
            break
        elif k=='fragments' and v>=250:
            inventory[k]-=250
            print(f"Valanyr obtained!")
            print(f"{k}: {v}")
            break
        elif k=='motes' and v>=250:
            inventory[k]-=250
            print(f"Dragonwrath obtained!")
            print(f"{k}: {v}")
            break