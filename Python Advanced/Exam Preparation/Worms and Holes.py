from collections import deque       #100/100

worms = list(map(int, input().split()))
length_of_worms = len(worms)
holes = deque(map(int, input().split()))
matches = 0

while True:
    if worms[-1]==holes.popleft():
        matches+=1
        worms.pop()
    else:
        worms[-1]-=3
        if worms[-1]<=0: worms.pop()
        
    if len(worms)==0 or len(holes)==0:
        
        if matches==0: print("There are no matches.")
        else: print(f"Matches: {matches}")
        
        if len(worms) == 0 and length_of_worms==matches:
            print("Every worm found a suitable hole!")
        elif len(worms)==0 and length_of_worms!=matches:
            print("Worms left: none")
        else: print(f"Worms left: {', '.join(list(map(str, worms)))}")    
        
        if len(holes)==0:
            print("Holes left: none")
        else:
            print(f"Holes left: {', '.join(list(map(str, holes)))}") 
        
        break
            
        