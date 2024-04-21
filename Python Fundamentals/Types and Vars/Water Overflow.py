n = int(input())
sum = 0
blackpoints = 0

for i in range(n):
    liters = int(input())
    sum+=liters
    if(sum>255): 
        sum-=liters
        blackpoints+=1
        
for blackpoint in range(blackpoints):
    print("Insufficient capacity!")
    
print(sum)