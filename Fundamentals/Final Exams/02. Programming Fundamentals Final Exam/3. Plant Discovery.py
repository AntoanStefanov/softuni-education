n = int(input())

plant_rarity_dict = {}
plant_rating_dict = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    plant_rarity_dict[plant] = int(rarity)
    plant_rating_dict[plant] = []


while True:
    info = input()
    if info == 'Exhibition':
        break
    info = info.split(': ')
    command = info[0]

    if command == 'Rate':
        plant, rating = info[1].split(' - ')
        rating = int(rating)
        if plant in plant_rating_dict:
            plant_rating_dict[plant].append(rating)
        else:
            print('error')
    elif command == 'Update':
        plant, new_rarity = info[1].split(' - ')
        if plant in plant_rarity_dict:
            new_rarity = int(new_rarity)
            plant_rarity_dict[plant] = new_rarity
        else:
            print('error')

    elif command == 'Reset':
        plant = info[1]
        if plant in plant_rating_dict:
            plant_rating_dict[plant] = []
        else:
            print('error')
    else:
        print('error')


new_dict_for_sort = {}

print('Plants for the exhibition:')

for plant, rarity in plant_rarity_dict.items():
    if len(plant_rating_dict[plant]) == 0:
        rating = 0
    else:
        rating = sum(plant_rating_dict[plant]) / len(plant_rating_dict[plant])
    new_dict_for_sort[plant] = [rarity, rating]


sorted_dict = sorted(new_dict_for_sort.items(),
                     key=lambda t: (-t[1][0], -t[1][1]))

for plant, info in sorted_dict:
    rarity = info[0]
    rating = info[1]
    print(f'- {plant}; Rarity: {rarity}; Rating: {rating:.2f}')
