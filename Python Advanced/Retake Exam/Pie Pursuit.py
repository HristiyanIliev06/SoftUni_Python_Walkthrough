from collections import deque   #100/100

contestants = deque(map(int, input().split()))
pies = list(map(int, input().split()))

while contestants and pies:
    current_contestant = contestants.popleft()
    current_pie = pies.pop()
    if current_contestant>=current_pie:
        current_contestant-=current_pie
        if current_contestant>0:
            contestants.append(current_contestant)
    else:
        current_pie-=current_contestant
        if current_pie>1 or not pies:
            pies.append(current_pie)
        elif current_pie==1:
            pies[-1]+=current_pie


if not pies and not contestants:
   print("We have a champion!")             
elif not pies:
    print("We will have to wait for more pies to be baked!" )
    print(f"Contestants left: {', '.join(str(contestant) for contestant in contestants)}")
elif not contestants:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(pie) for pie in pies)}")
