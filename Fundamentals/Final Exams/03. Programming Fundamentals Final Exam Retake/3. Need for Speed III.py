number_of_cars = int(input())
km = {}
fuel = {}
for car in range(number_of_cars):
    name, mileage, gas = input().split('|')
    mileage = int(mileage)
    gas = int(gas)
    km[name] = mileage
    fuel[name] = gas
while True:
    command = input()
    if command == 'Stop':
        break

    info = command.split(' : ')
    command = info[0]
    car = info[1]

    if command == 'Drive':
        distance = int(info[2])
        gas = int(info[3])
        if gas > fuel[car]:
            print('Not enough fuel to make that ride')
        else:
            km[car] += distance
            fuel[car] -= gas
            print(
                f"{car} driven for {distance} kilometers. {gas} liters of fuel consumed.")
        if km[car] >= 100_000:
            del km[car]
            del fuel[car]
            print(f'Time to sell the {car}!')
    elif command == 'Refuel':
        gas = int(info[2])
        if fuel[car] + gas > 75:
            refueled = 75 - fuel[car]
            fuel[car] = 75
        else:
            fuel[car] += gas
            refueled = gas
        print(f"{car} refueled with {refueled} liters")

    elif command == 'Revert':
        kilometers = int(info[2])
        km[car] -= kilometers
        if km[car] < 10_000:
            km[car] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")


sorted_cars = dict(sorted(km.items(), key=lambda tpl: (-tpl[1], tpl[0])))
for car, km in sorted_cars.items():
    print(f"{car} -> Mileage: {km} kms, Fuel in the tank: {fuel[car]} lt.")
