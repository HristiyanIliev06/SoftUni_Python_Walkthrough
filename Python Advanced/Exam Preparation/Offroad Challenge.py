from collections import deque

fuel = list(map(int, input().split()))
consumption_indexes = deque(map(int, input().split()))
needed_quantities = deque(map(int, input().split()))
reached = 0
altitudes = []

for _ in range(4):
    
    if fuel[-1] - consumption_indexes[0] >= needed_quantities[0]:
        reached+=1
        altitudes.append(f"Altitude {reached}")
        print(f"John has reached: Altitude {reached}")
        fuel.pop()
        consumption_indexes.popleft()
        needed_quantities.popleft()
    elif fuel[-1] - consumption_indexes[0] < needed_quantities[0] and reached==0:
        print("John failed to reach the top.\nJohn didn't reach any altitude.")
        break
    elif fuel[-1] - consumption_indexes[0] < needed_quantities[0] and 4>reached>0:
        print(f"John did not reach: Altitude {reached+1}\nJohn failed to reach the top.\nReached altitudes: {', '.join(altitudes)}")
        break
        
    if reached==4:
        print("John has reached all the altitudes and managed to reach the top!")