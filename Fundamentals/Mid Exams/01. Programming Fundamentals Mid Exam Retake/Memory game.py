sequence = input().split()
moves = 0
while True:

    data = input()

    if data == 'end':
        break
    data = data.split()
    first_index = int(data[0])
    second_index = int(data[1])
    moves += 1

    # Ще мине и без това след второто and :) , тоест ако и двата дадени индекса са еднакви !
    if 0 <= first_index < len(sequence) and 0 <= second_index < len(sequence) and first_index != second_index:

        if sequence[first_index] == sequence[second_index]:
            print(
                f"Congrats! You have found matching elements - {sequence[first_index]}!")
            element = sequence[first_index]
            while element in sequence:
                sequence.remove(element)
        elif not sequence[first_index] == sequence[second_index]:
            print("Try again!")

    else:
        middle = len(sequence) // 2
        element = f'-{moves}a'
        sequence.insert(middle, element)
        sequence.insert(middle, element)
        print("Invalid input! Adding additional elements to the board")

    if not sequence:
        print(f"You have won in {moves} turns!")
        break
if sequence:
    print("Sorry you lose :(")
    print(*sequence)
