data_base = {}
def register(name:str, lpn:str):
    if name not in data_base.keys():
        data_base[name] = lpn
        return f"{name} registered {lpn} successfully"
    else: return f"ERROR: already registered with plate number {lpn}"
    
def unregister(name:str):
    if name in data_base.keys():
        data_base.pop(name)
        return f"{name} unregistered successfully"
    else: return f"ERROR: user {name} not found"

n = int(input())
for _ in range(n):
    data = input().split()
    if data[0]=="register": print(register(data[1], data[2]))
    elif data[0]=="unregister":print(unregister(data[1]))
    
for (k, v) in data_base.items(): print(f"{k} => {v}")