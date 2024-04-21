index1 = int(input())
index2 = int(input())
result = ""

for i in range(index1, index2+1):
    result+=(chr(i)+" ")
print(result)