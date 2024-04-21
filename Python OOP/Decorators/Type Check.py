def type_check(Type:type):
    def decorator(func):
        def wrapper(x):
            if type(x)!=Type:
                return 'Bad Type'
            
            return func(x)
        
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

