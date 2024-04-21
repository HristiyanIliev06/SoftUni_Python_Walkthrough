n = int(input())
even_set = set({})
odd_set = set({})
osum = 0
esum = 0

for i in range(n):
    sum=0
    name = input()
    
    for char in name:
        sum+=ord(char)
        
    if (sum//(i+1))%2!=0:
        osum+=sum//(i+1)
        odd_set.add(sum//(i+1))
    else:
        
        esum+=sum//(i+1)
        even_set.add(sum//(i+1))
        
if osum==esum: print(*odd_set.union(even_set), sep=", ")
elif osum>esum: print(*odd_set.difference(even_set), sep=", ")
elif osum<esum: print(*odd_set.symmetric_difference(even_set), sep=", ")
    