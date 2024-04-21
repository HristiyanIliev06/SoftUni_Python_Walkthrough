from project.dark_knight import DarkKnight

class BladeKnight(DarkKnight):
    
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)
        
    def __str__(self) -> str:
        return super().__str__()