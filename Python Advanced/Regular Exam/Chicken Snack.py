from collections import deque   #100/100

budget = list(map(int, input().split()))
prices = deque(map(int, input().split()))
eaten = 0

while budget and prices:
    if budget[-1]==prices[0]:
        eaten+=1
        budget.pop()
        prices.popleft()
    elif budget[-1]>prices[0]:
        eaten+=1
        leftover = budget.pop()-prices.popleft()
        if len(budget)>0:
            budget[-1]+=leftover
    elif budget[-1]<prices[0]:
        budget.pop()
        prices.popleft()
        
if eaten==0:
    print("Henry remained hungry. He will try next weekend again.")
elif eaten==1:
    print(f"Henry ate: {eaten} food.")
elif 1<eaten<4:
    print(f"Henry ate: {eaten} foods.")
elif eaten>=4:
    print(f"Gluttony of the day! Henry ate {eaten} foods.")