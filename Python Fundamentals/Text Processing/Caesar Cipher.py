message = input()
encrypted_message = ""

for char in message:
    encrypted_message+=chr(ord(char)+3)
    
print(encrypted_message)