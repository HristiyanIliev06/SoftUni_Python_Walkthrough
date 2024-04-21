first = input().split(", ")
second = input().split(", ")
result = []

for i in range(len(first)):
    for j in range(len(second)):
        if first[i] in second[j] and first[i] not in result: result.append(first[i])
    #result =[first[i] for j in range(len(second)) if first[i] in second[j] and first[i] not in result]
    #LIST COMPREHENSION НЕ РАБОТИ ПО ОЧАКВАНИЯТА, КОГАТО Е В ДРУГ ЦИКЪЛ    
    
print(result)