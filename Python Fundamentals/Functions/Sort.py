def sequence(Ns:list):
    Ns.sort()
    return Ns 

Ns = list(map(int, input().split()))
print(sequence(Ns))
