string = input()
items = {}

for char in string:
    if char!=" " and string.count(char):
        items[char] = string.count(char)

for key in items:       
    print(f"{key} -> {items[key]}")