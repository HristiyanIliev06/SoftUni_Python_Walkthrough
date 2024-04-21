n=int(input())

for i in range(n):
    str = input()
    x = 0
    for j in range(len(str)):
        if str[j]=='.' or str[j]=='_' or str[j]==',':
            x+=1          
    if not x>0: print(f"{str} is pure.")
    else: print(f"{str} is not pure!")