contacts = {}
while True:
    phonenumbers = input().split('-')
    if phonenumbers[0].isdigit():
        N = phonenumbers[0]
        break
    contacts[phonenumbers[0]] = phonenumbers[1]

for _ in range(int(N)):
    name = input()
    if name not in contacts:
        print(f"Contact {name} does not exist.")
    else: print(f"{name} -> {contacts[name]}" )