from  math import ceil as c

class PhotoAlbum:
    photos = []
    
    def __init__(self, pages:int) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
    
    @classmethod    
    def from_photos_count(cls, photos_count:int):
        return cls(c(photos_count/4)) 
    
    def add_photo(self, label: str):
        
        for i in range(self.pages):
            if len(self.photos[i])<4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i+1} slot {self.photos[i].index(label)+1}"
            else: 
                continue
            
        return "No more free slots"
    
    def display(self):
        result = []
        for i in range(len(self.photos)):
            result.append(11*'-')
            result.append(('[] ' * len(self.photos[i])).strip())
                
        result.append(11*'-')        
            
        return '\n'.join(result)
        
        
album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())