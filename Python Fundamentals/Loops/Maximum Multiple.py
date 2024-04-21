div = int(input())
b = int(input())

for N in range(b,div-1,-1):
    if N % div == 0: 
        print(N)
        break