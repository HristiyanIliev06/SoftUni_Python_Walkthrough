words = input().split()

evens = [word for word in words if len(word)%2==0]

print("\n".join(evens))