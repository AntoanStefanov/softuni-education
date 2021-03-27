number_of_cars = int(input())

parking_lot = set()

for _ in range(number_of_cars):
    direction, car_number = input().split(', ')
    # Dictionary
    directions = {
        'IN': parking_lot.add,
        # Remove method will return keyerror if the car does not exist in the set.
        # Discard method will ignore if we remove a car that doesn't exist in the set
        # Yet judge gives 100/100 with remove
        # We can use if statement to check if the car exists in the set
        # And then remove method , if it doesn't exist in the set, Do nothing
        # Which is equal to discard method.
        'OUT': parking_lot.discard,

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
