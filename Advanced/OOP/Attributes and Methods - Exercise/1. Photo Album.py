class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)


    def add_photo(self, label):
        for p_index, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                slot_index = page.index(label)
                return f"{label} photo added successfully on page {p_index + 1} slot {slot_index + 1}"
        return "No more free spots"

    def display(self):
        res = '-----------\n'
        for page in self.photos:
            photos = [photos.append('[]') for _ in page]    
            res += ' '.join(photos)
            res += '\n-----------\n'
        return res


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
