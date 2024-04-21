def ispalindrome(nums:list)->bool:
    check = False
    checks = []
    for num in nums:
        reversed_num = 0
        n = num
        while n!=0:
            digit=n%10
            reversed_num=reversed_num*10+digit
            n//=10
        if num==reversed_num: check=True
        else: check=False
        checks.append(check)
    return checks


nums = list(map(int, input().split(", ")))
for i in ispalindrome(nums): print(i)