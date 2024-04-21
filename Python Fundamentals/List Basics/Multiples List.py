factor = int(input())
count = int(input())
x_list = list()

for i in range(factor,count*factor+1,factor):
    x_list.append(i)
    
print(x_list)