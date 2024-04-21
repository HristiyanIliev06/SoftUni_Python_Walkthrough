data_base = {}

def gather(course, name):
    if course not in data_base.keys():
        data_base[course] = []
        data_base[course].append(name)
    else:
        data_base[course].append(name)

while True:
    data = input().split(' : ')
    if(data[0]=='end'): break
    gather(data[0], data[1])
    
for k, v in data_base.items():
    print(f"{k}: {len(v)}")
    for item in v:
        print(f"-- {item}")