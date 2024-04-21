def sequence(ints:list):
    result = list(filter(lambda x: x%2==0, ints))
    return result

ints = list(map(int, input().split()))
print(sequence(ints))