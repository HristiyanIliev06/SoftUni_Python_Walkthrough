def movie_organizer(*args):
    string_builder = ""
    for arg, erg in args:
        string_builder+=f"{arg} - {erg} "        
    return string_builder.strip()
    
    

print(movie_organizer(("The Matrix", "Sci-fi"),("Thex", "Sci-fi"),("The Matrix", "Sfi")))