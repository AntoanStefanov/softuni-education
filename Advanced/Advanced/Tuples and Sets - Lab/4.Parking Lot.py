number_of_cars = int(input())

parking_lot = set()

for _ in range(number_of_cars):
    direction, car_number = input().split(', ')
    # Dictionary
    directions = {
        'IN': parking_lot.add,
        'OUT': parking_lot.remove,

    }
    directions[direction](car_number)
     ### OR ### 
     
    # if direction == 'IN':
    #     parking_lot.add(car_number)
    # else:
    #     parking_lot.remove(car_number)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print('Parking Lot is Empty')
