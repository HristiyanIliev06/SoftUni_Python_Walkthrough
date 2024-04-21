def password_validator(password):
    passed = False
    num_of_digits = 0
    check_marks = 0
    messages = []
    if 6>len(password) or len(password)>10: messages.append("Password must be between 6 and 10 characters")
    else: check_marks+=1     
    for char in password:
        if char.isdigit()==False and char.isalpha()== False: 
            messages.append("Password must consist only of letters and digits")
            passed = False
            break
        else: passed=True
    if passed: check_marks+=1
    for char in password:
        if char.isdigit(): num_of_digits+=1
    if num_of_digits<2: messages.append("Password must have at least 2 digits")
    else: check_marks+=1
    
    if check_marks==3: return "Password is valid"
    else: return messages

password = input()   
if password_validator(password)!="Password is valid":
    for message in password_validator(password): print(message)
else: print(password_validator(password))