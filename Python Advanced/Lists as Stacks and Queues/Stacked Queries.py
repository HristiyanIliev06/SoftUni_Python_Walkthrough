n = int(input())
stack = []
new_stack = []

for _ in range(n):
    query = list(map(int, input().split()))
    if query[0]==1: stack.append(query[1])
    elif query[0]==2 and len(stack)>0: stack.pop()
    elif query[0]==3 and len(stack)>0: print(max(stack))
    elif query[0]==4 and len(stack)>0: print(min(stack))
            
while stack:
    new_stack.append(str(stack.pop()))
    
print(', '.join(new_stack))