cities = {}
while True:
    data = input()
    if data == 'Sail':
        break
    data = data.split('||')

    city, population, gold = data
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {}
        cities[city]['population'] = population
        cities[city]['gold'] = gold
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

while True:
    data = input()
    if data == 'End':
        break
    data = data.split('=>')
    command = data[0]
    if command == 'Plunder':
        city = data[1]
        people = int(data[2])
        gold = int(data[3])

        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        cities[city]['population'] -= people
        cities[city]['gold'] -= gold

        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif command == 'Prosper':
        city = data[1]
        gold = int(data[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[city]['gold'] += gold
            print(
                f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

if cities:
    print(
        f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    # print sorted_cities to get a better view ,
    # cities.items() returns a tuple with the dict keys and values
    sorted_cities = sorted(
        cities.items(), key=lambda tuple: (-tuple[1]['gold'], tuple[0]))

    for city, info in sorted_cities:

        population = info['population']
        gold = info['gold']
        print(
            f'{city} -> Population: {population} citizens, Gold: {gold} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
