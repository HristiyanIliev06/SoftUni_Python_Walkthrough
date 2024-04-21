def is_perfect_number(num:int)->str:
    sum=0
    for n in range(1, num):
        if num%n==0: sum+=n
    if sum==num: return "We have a perfect number!"
    else: return "It's not so perfect."
    
num = int(input())
print(is_perfect_number(num))