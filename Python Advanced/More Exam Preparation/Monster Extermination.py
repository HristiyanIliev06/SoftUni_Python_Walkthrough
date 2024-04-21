from collections import deque   #50/100

armor_values = deque(map(int, input().split(',')))
s_s_impact_values = list(map(int, input().split(',')))
killed_monsters = 0

while armor_values and s_s_impact_values: 
    if armor_values[0]<s_s_impact_values[-1]:
        result = s_s_impact_values.pop()-armor_values.popleft()
        try:
            s_s_impact_values[0]+=result
        except(IndexError):
            s_s_impact_values.append(result)
        killed_monsters+=1
    elif armor_values[0]==s_s_impact_values[-1]:
        s_s_impact_values.pop()
        armor_values.popleft()
        killed_monsters+=1 
    else:
        result = armor_values.popleft()-s_s_impact_values.pop()
        armor_values.append(result)
        
    if len(armor_values)==0:
        print("All monsters have been killed!")
    elif len(s_s_impact_values)==0:
        print("The soldier has been defeated.")
        
print(f"Total monsters killed: {killed_monsters}")