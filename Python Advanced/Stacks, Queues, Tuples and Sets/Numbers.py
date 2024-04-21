first = set(map(int, input().split()))
second = set(map(int, input().split()))

for _ in range(int(input())):
    action1, action2, *data = input().split()
    actions = action1+" "+action2
    if actions=="Add First":
        [first.add(int(item)) for item in data]
    elif actions=="Add Second":
        [second.add(int(item)) for item in data]
    elif actions=="Remove First":
        [first.discard(int(item)) for item in data]
    elif actions=="Remove Second":
        [second.discard(int(item)) for item in data]
    elif actions=='Check Subset':
        print(first.issubset(second) or second.issubset(first))


print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
