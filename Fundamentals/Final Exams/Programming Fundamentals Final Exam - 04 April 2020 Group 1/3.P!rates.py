targeted_cities_population = {}
targeted_cities_gold = {}


while True:
    command = input()
    if command == "Sail":
        break
    targeted_city, population, gold = command.split("||")
    if targeted_city not in targeted_cities_population:
        targeted_cities_population[targeted_city] = 0
    targeted_cities_population[targeted_city] += int(population)

    if targeted_city not in targeted_cities_gold:
        targeted_cities_gold[targeted_city] = 0
    targeted_cities_gold[targeted_city] += int(gold)


while True:
    event = input()
    if event == "End":
        break
    elif "Plunder" in event:
        action, targeted_city, population, gold = event.split("=>")
        population = int(population)
        gold = int(gold)

        targeted_cities_population[targeted_city] -= population
        targeted_cities_gold[targeted_city] -= gold
        print(
            f"{targeted_city} plundered! {gold} gold stolen, {population} citizens killed.")

        if targeted_cities_population[targeted_city] == 0 or targeted_cities_gold[targeted_city] == 0:
            del targeted_cities_population[targeted_city]
            del targeted_cities_gold[targeted_city]
            print(f"{targeted_city} has been wiped off the map!")

    else:
        action, targeted_city, gold = event.split("=>")
        gold = int(gold)

        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue

        targeted_cities_gold[targeted_city] += gold
        total_gold = targeted_cities_gold[targeted_city]
        print(
            f"{gold} gold added to the city treasury. {targeted_city} now has {total_gold} gold.")


if len(targeted_cities_population) > 0:
    print(
        f"Ahoy, Captain! There are {len(targeted_cities_gold)} wealthy settlements to go to:")

    sorted_targeted_cities_gold = dict(
        sorted(targeted_cities_gold.items(), key=lambda t: (-t[1], t[0])))

    for targeted_city, gold in sorted_targeted_cities_gold.items():
        print(
            f"{targeted_city} -> Population: {targeted_cities_population[targeted_city]} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
