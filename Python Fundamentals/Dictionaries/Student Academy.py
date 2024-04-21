grading = {}
n = int(input())

for i in range(2*n):
    data = input()
    if i%2==0:
        key = data
    else:
        value = float(data)
        if key not in grading.keys():
            grading[key] = []
            grading[key].append(value)
        else: grading[key].append(value)
        
for k, v in grading.items():
    total = 0
    for item in v:
        total+=item
    if total/len(v)>=4.50:
        print(f"{k} -> {total/len(v):.2f}")