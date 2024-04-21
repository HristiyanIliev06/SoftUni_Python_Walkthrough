rows = int(input())
matrix = [int(num) for num in input().split(', ') for _ in range(rows)]
primary_d = []
secondary_d = []

"""for r in range(rows):
    for c in range(rows):
        primary_d.append(str(matrix[r][c]))
        
for r in range(rows):
    for c in range(-rows):
        secondary_d.append(str(matrix[r][c]))
        
print(f'Primary diagonal: {", ".join(primary_d)}.', end=' ')
print(f'Sum: {sum(int(primary_d))}')"""