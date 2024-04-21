electrons = int(input())
capacity = 0
n = 0
max = 0
inventory = []
reserve = 0

while electrons>0:
    n+=1
    max =2*n**2
    electrons-=max
    if electrons>=0:
        inventory.append(max)
    else:
        reserve = electrons
        for e in range(reserve, 0):
            electrons+=1
            max-=1
        inventory.append(max)
        
print(inventory)