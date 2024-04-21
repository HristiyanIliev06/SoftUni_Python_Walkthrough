import math

sequence = list(map(int, input().split(', ')))
max_value = math.ceil(max(sequence)/10)*10
list_of_nums = []

for group in range(10, max_value+1, 10):
    list_of_nums = list(filter(lambda x: x<=group, sequence))
    for item in list_of_nums:
        if item in sequence: sequence.remove(item)
    print(f"Group of {group}'s: {list_of_nums}")