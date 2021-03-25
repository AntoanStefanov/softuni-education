number_of_pieces = int(input())

piece_composer_dict = {}
piece_key_dict = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    piece_composer_dict[piece] = composer #### Mosh way
    piece_key_dict[piece] = key


while True:
    data = input()
    if data == 'Stop':
        break

    data = data.split('|')
    command = data[0]
    if command == 'Add':
        piece_to_add = data[1]
        composer_to_add = data[2]
        key_to_add = data[3]

        if piece_to_add in piece_composer_dict:
            print(f"{piece_to_add} is already in the collection!")
        else:
            piece_composer_dict[piece_to_add] = composer_to_add
            piece_key_dict[piece_to_add] = key_to_add
            print(
                f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")

    elif command == 'Remove':
        piece_to_remove = data[1]
        if piece_to_remove in piece_composer_dict:
            del piece_composer_dict[piece_to_remove]
            del piece_key_dict[piece_to_remove]
            print(f'Successfully removed {piece_to_remove}!')
        else:
            print(
                f"Invalid operation! {piece_to_remove} does not exist in the collection.")
    elif command == 'ChangeKey':
        piece_to_change_key = data[1]
        new_key = data[2]

        if piece_to_change_key in piece_composer_dict:
            piece_key_dict[piece_to_change_key] = new_key
            print(f"Changed the key of {piece_to_change_key} to {new_key}!")
        else:
            print(
                f"Invalid operation! {piece_to_change_key} does not exist in the collection.")


piece_composer_dict = sorted(
    piece_composer_dict.items(), key=lambda tuple: (tuple[0], tuple[1]))

for piece, composer in piece_composer_dict:
    print(f"{piece} -> Composer: {composer}, Key: {piece_key_dict[piece]}")
