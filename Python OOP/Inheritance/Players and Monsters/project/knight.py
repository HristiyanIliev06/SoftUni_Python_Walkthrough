from project.hero import Hero

class Knight(Hero):
    
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)
        
    def __str__(self) -> str:
        return super().__str__()