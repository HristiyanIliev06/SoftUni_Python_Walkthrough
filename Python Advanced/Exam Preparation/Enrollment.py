def gather_credits(credits_number, *args): #100/100
    enrolled = 0
    passed = []
    
    for tuple in args:
        if enrolled >= credits_number: #добавено
            break                      #добавено
        if tuple[0] in passed:         #добавено
            continue                   #добавено
        passed.append(tuple[0])
        enrolled+=tuple[1]
    
    if enrolled>=credits_number:
        return f"Enrollment finished! Maximum credits: {enrolled}.\nCourses: {', '.join(sorted(passed))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_number-enrolled} credits more."
        
print(gather_credits(

60,

("Basics", 27),

("Fundamentals", 27),

("Advanced", 30)

))