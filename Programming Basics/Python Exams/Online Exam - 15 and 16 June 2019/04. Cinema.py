free_seats = int(input())

command = input()
total_taken_seats = 0
total_tickets_price = 0
while command != "Movie time!":
    taken_seats = int(command)
    total_taken_seats += taken_seats
    if total_taken_seats > free_seats:
        print("The cinema is full.")
        break
    tickets_price = taken_seats * 5
    if taken_seats % 3 == 0:
        tickets_price -= 5
    total_tickets_price += tickets_price

    command = input()
else:
    print(
        f"There are {free_seats - total_taken_seats} seats left in the cinema.")

print(f"Cinema income - {total_tickets_price} lv.")
