number_of_cars = int(input())

parking_lot = set()

for _ in range(number_of_cars):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if parking_lot:
    for car_number in parking_lot:
        print(car_number)
else:
    print('Parking Lot is Empty')
