data_base = {}

def unique(l:list):
    unique_list = []
    for item in l:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

while True:
    enter = input().split(' -> ')
    if(enter[0]=='End'): break
    
    company = enter[0]
    e_id = enter[1]
    if company not in data_base.keys():
        data_base[company] = []
        data_base[company].append(e_id)
    else: data_base[company].append(e_id)
    
for k, v in data_base.items():
    print(k)
    for item in unique(v):
        print(f"-- {item}")