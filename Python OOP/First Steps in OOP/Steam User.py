class SteamUser:
    played_hours = 0
    count = 0
    def __init__(self, un:str, g:list):
        self.username = un
        self.games = g
        self.count+=1
        
    def play(self, game:str, hours:int)->str:
        if game in self.games:
            SteamUser.played_hours+=hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"
                
    def buy_game(self, game:str):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"
    
    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
    
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())

        