countries = input().split(', ')
capitals = input().split(', ')

corresponse = {countries[i]:capitals[i] for i in range(len(countries))}
for country, capital in corresponse.items():
    print(f"{country} -> {capital}")
