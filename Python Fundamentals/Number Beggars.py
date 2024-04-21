List = input().split(", ")
beggars = int(input())
start = 0
result = list()

for beggar in range(beggars):
    sum = 0
    for i in range(start, len(List), beggars):
        sum += int(List[i])
    start+=1
    result.append(sum)
    
print(result)