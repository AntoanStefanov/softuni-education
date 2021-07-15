from math import ceil
class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)
    

    def add_photo(self, label):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < 4:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        res = ''
        for row in range(len(self.photos)):
            res += '-' * 11 + '\n'
            res += f"{' '.join(['[]' for photo in self.photos[row]])}\n"
        res += '-' * 11 + '\n'
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
