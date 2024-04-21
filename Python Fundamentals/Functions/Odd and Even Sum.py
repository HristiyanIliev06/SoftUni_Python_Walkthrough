def odd_and_even(n:int):
    total = []
    even_total = 0
    odd_total = 0
    while n>0:
        total.append(n%10)
        n//=10
    #even_total = sum(total, lambda x: x%2==0)
    #odd_total = sum(total, lambda x: x%2!=0)
    # ЛАМБДА ФУНКЦИИТЕ НЕ РАБОТЯ СЪС СУМИРАНЕ, А ГЛАВНО СЪС СОРТИРАНЕ!!!
    for num in total:
        if num%2==0: even_total+=int(num)
        else: odd_total+=int(num)
    return f"Odd sum = {odd_total}, Even sum = {even_total}"

n = int(input())
print(odd_and_even(n))