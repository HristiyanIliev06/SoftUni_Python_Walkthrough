from project.dark_wizard import DarkWizard

class SoulWizard(DarkWizard):
    
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)
        
    def __str__(self) -> str:
        return super().__str__()