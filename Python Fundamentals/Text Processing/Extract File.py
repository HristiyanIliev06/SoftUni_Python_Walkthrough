file = input().split('.')
extension = file[1]
before_extension = file[0].split('\\')
name = before_extension[-1]

print(f"File name: {name}")
print(f"File extension: {extension}")