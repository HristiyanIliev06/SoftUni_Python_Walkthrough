n = int(input())
set_of_chemicals = set([])

for _ in range(n):
    chemicals = input().split()
    for chemical in chemicals:
        set_of_chemicals.add(chemical)
        
print(*set_of_chemicals, sep='\n')