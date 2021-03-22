waiting_people = int(input())
lift = [int(x) for x in input().split()]

for index, people in enumerate(lift):
    if people < 4:
        available_seats = 4 - people
        if waiting_people >= available_seats:
            waiting_people -= available_seats
            lift[index] += available_seats
        else:
            lift[index] += waiting_people
            waiting_people -= waiting_people

for people in lift:
    if people < 4:
        print("The lift has empty spots!")
        break
else:
    if waiting_people:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
print(*lift)
