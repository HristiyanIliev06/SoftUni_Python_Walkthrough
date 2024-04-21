line = list(map(int,input().split()))
n = int(input())

the_line = line.copy()
line.sort()
for index in range(n):
    the_line.remove(line[index])   
print(*the_line, sep=', ')
