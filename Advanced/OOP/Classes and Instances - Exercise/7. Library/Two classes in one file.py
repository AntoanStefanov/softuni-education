class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {author: list of books}
        self.rented_books = {}  # {usernames: {book names: days left}}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if not user in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        if user in self.rented_books:
            self.rented_books.pop(user.username)

    def change_username(self, user_id, new_username):
        for user in self.user_records:
            if user.username != new_username and user_id == user.user_id:
                if user.username in self.rented_books:
                    self.rented_books[new_username] = self.rented_books.pop(
                        user.username)
                user.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            if user.username == new_username and user_id == user.user_id:
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        for username, books_info in library.rented_books.items():
            if book_name in books_info:
                return f'The book "{book_name}" is already rented and will be available in {library.rented_books[username][book_name]} days!'

        for author_of_books, books in library.books_available.items():
            if book_name in books and author == author_of_books:
                self.books.append(book_name)
                if self.username not in library.rented_books:
                    library.rented_books[self.username] = {}
                library.rented_books[self.username][book_name] = days_to_return
                library.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, library):
        if book_name in self.books:
            del library.rented_books[self.username][book_name]
            library.books_available[author].append(book_name)
            self.books.remove(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return f'{", ".join(sorted(self.books))}'

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"


user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}')
 for user_record in library.user_records]

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})


user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.info())
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)
