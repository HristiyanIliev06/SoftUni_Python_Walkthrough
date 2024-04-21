clothes = list(map(int, input().split()))
capacity = int(input())
rack = 0
racks = 0

while clothes:
    piece = clothes.pop()
    if capacity<rack+piece:
        racks+=1
        rack=0
        rack+=piece
    else: rack+=piece
    
    if rack<capacity: continue
    elif rack==capacity:
        racks+=1
        rack=0
        
if rack>0: racks+=1

print(racks)