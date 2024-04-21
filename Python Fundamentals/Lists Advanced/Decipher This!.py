secret_message = input().split()
digits = ""
letter_occurances = 0
deciphered = []
new = ""
second = ""
last = ""
middle = ""

for word in secret_message:
    digits = ""
    letter_occurances = 0
    new = ""
    middle=""
    for char in word:
        if letter_occurances!=0: letter_occurances+=1
        if char.isdigit(): digits+=char
        if char.isalpha() and letter_occurances==0:
            letter_occurances+=1
            last = char
            second = word[-1]
        elif char.isalpha() and letter_occurances!=0 and letter_occurances<len(word)-len(digits): middle+=char
    new+=chr(int(digits))+second+middle+last
    deciphered.append(new)
        
print(" ".join(deciphered))
