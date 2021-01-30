name_book = input()
count = -1
while name_book != "No More Books":
    if count == -1:
        fav_book = name_book
    count += 1
    name_book = input()
    if fav_book == name_book:
        break
if fav_book == name_book:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")

############# OR #############

searched_book = input()
book = input()

checked_books = 0
while book != "No More Books" and book != searched_book:
    checked_books += 1
    book = input()
if book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
elif book == searched_book:
    print(f"You checked {checked_books} books and found it.")


########### OR ############

book_name = input()
book_count = 0
is_book_found = False

current_book = input()
while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1
    current_book = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
