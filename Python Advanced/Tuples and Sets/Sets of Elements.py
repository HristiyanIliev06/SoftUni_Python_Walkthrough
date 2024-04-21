length_of_sets = input().split()
n = int(length_of_sets[0])
m = int(length_of_sets[1])

n_set = set([])
m_set = set([])

for _ in range(n):
    num = input()
    n_set.add(num)
    
for _ in range(m):
    num = input()
    m_set.add(num)
    
print('\n'.join(n_set & m_set) )