

def add_user(book, side, user):

    if side not in book:
        book[side] = []

    all_users = [user for users_list in book.values() for user in users_list]

    if user not in all_users:
        book[side].append(user)


def transfer_user(book, side, user):

    if side not in book:
        book[side] = []

    book[side].append(user)


def change_side(book, side, user):
    does_exist = False
    for user_side, users in book.items():
        if user in users:
            does_exist = True
            book[user_side].remove(user)
            transfer_user(book, side, user)
            break

    if not does_exist:
        add_user(book, side, user)
    print(f"{user} joins the {side} side!")


book = {}

while True:

    data = input()

    if data == 'Lumpawaroo':
        break

    if '|' in data:
        side, user = data.split(' | ')

        add_user(book, side, user)

    else:
        user, side = data.split(' -> ')

        change_side(book, side, user)


sorted_book = dict(sorted(book.items(), key=lambda x: ((-len(x[1]), x[0]))))

for side, users in sorted_book.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")

        for user in sorted(users):
            print(f'! {user}')
