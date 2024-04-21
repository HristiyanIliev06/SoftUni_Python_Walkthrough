n = int(input())
longest_intersection = set({})
li_length = 0

for _ in range(n):
    data = input().split('-')
    left = data[0].split(',')
    right = data[1].split(',')
    f_start = int(left[0])
    f_end = int(left[1])
    s_start = int(right[0])
    s_end = int(right[1])
    
    f_set = {i for i in range(f_start,f_end+1)}
    s_set = {i for i in range(s_start,s_end+1)}
    intersection = f_set & s_set
    
    if li_length<len(intersection):
        li_length=len(intersection)
        longest_intersection = intersection
        
print(f"Longest intersection is {list(longest_intersection)} with length {li_length}")
