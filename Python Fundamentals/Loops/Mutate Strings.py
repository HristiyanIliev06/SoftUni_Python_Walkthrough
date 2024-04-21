first = input()
second = input()
last=first

for char in range(len(first)):
    left=second[:char+1]
    right=first[char+1:]
    new=left+right
    if new!=last:
        print(new)
        last=new