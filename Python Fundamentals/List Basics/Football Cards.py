A = ['A-1','A-2','A-3','A-4','A-5','A-6','A-7','A-8','A-9','A-10','A-11']
B = ['B-1','B-2','B-3','B-4','B-5','B-6','B-7','B-8','B-9','B-10','B-11']

info = input().split()
status = True

for player in info:
    if player in A: A.remove(player)
    elif player in B: B.remove(player)
    if len(A)< 7 or len(B)<7: 
        status = False 
        break
    
print(f"Team A - {len(A)}; Team B - {len(B)}")
if status==False: print("Game was terminated")
