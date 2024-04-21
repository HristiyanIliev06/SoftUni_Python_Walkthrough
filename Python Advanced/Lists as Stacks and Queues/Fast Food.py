from collections import deque

quantity = int(input())
quantity_by_order = deque(map(int, input().split()))

print(max(quantity_by_order))
for order in list(quantity_by_order):
    if order<=quantity:
        quantity_by_order.popleft()
        quantity-=order
    else: break
 
if len(quantity_by_order)==0:     
    print("Orders complete")
else:
    print("Orders left:", end=' ')
    print(*quantity_by_order)