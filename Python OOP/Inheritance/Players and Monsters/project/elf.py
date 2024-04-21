from  project.hero import Hero

class Elf(Hero):
    
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)
        
    def __str__(self) -> str:
        return super().__str__()
    
"""hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))"""
