number = int(input())

plants_dict = {}

for _ in range(number):
    plants = input().split('<->')
    plant = plants[0]
    rarity = float(plants[1])

    plants_dict[plant] = {'rarity': rarity, 'rating': []}

commands = input()

while not commands == 'Exhibition':
    commands_split = commands.split()
    command = commands_split[0]
    plant = commands_split[1]

    try:
        if command == 'Rate:':
            rating = float(commands_split[3])

            plants_dict[plant]['rating'].append(rating)

        elif command == 'Update:':
            new_rarity = float(commands_split[3])

            plants_dict[plant]['rarity'] = new_rarity

        elif command == 'Reset:':

            plants_dict[plant]['rating'] = []
    except:
        print('error')

    commands = input()

for key, value in plants_dict.items():
    if len(plants_dict[key]['rating']) == 0:
        plants_dict[key]['rating'] = 0
    else:
        plants_dict[key]['rating'] = sum(
            plants_dict[key]['rating']) / len(plants_dict[key]['rating'])

plants_dict_sort = sorted(plants_dict.items(), key=lambda x: (
    x[1]['rarity'], x[1]['rating']), reverse=True)

print('Plants for the exhibition:')

for plant_tup in plants_dict_sort:
    print(
        f' - {plant_tup[0]}; Rarity: {plant_tup[1]["rarity"]:.0f}; Rating: {plant_tup[1]["rating"]:.2f}')
