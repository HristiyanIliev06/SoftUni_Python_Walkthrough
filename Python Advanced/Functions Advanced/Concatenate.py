def concatenate(*args, **kwargs):
    concatenated = ""
    for arg in args:
       concatenated+=arg

    for k, v in kwargs.items():
        if k in concatenated:
            concatenated = concatenated.replace(k, v)
            
    return concatenated

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java')) 