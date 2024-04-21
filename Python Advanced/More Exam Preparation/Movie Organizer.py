def movie_organizer(*args): #100/100
    genre_movies = {}
    string_builder = ""
    for movie, genre in args:
        if genre not in genre_movies.keys():
            genre_movies[genre] = []
                
        genre_movies[genre].append(movie)
            
    for genre, movies in sorted(genre_movies.items(), key= lambda kvp: (-len(kvp[1]), kvp[0])):
        string_builder+=f"{genre} - {len(genre_movies[genre])}\n"
        for movie in sorted(movies):
            string_builder+=f"* {movie}\n"
            
    return string_builder.strip()
                
    













print(movie_organizer(("The Matrix", "Sci-fi")))

print(movie_organizer(

("The Godfather", "Drama"),

("The Hangover", "Comedy"),

("The Shawshank Redemption",

"Drama"),

("The Pursuit of Happiness",

"Drama"),

("The Hangover Part II", "Comedy"))) 


print(movie_organizer(("Avatar: The Way of Water", "Action"), ("House Of Gucci", "Drama"), ("Top Gun", "Action"), ("Ted", "Comedy"), ("Duck Soup", "Comedy"), ("The Dark Knight", "Action"), ("A Star Is Born", "Musicals"), ("The Warrior", "Action"), ("Like A Boss", "Comedy"), ("The Green Mile", "Drama"), ("21 Jump Street", "Comedy")))