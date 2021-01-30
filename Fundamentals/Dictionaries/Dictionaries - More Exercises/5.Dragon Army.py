def parse_stats(damage, health, armor):
    if damage == 'null':
        damage = 45
    else:
        damage = int(damage)
    if health == 'null':
        health = 250
    else:
        health = int(health)
    if armor == 'null':
        armor = 10
    else:
        armor = int(armor)

    return damage, health, armor


army = {}

n = int(input())


for i in range(n):

    dragon_type, name, damage, health, armor = input().split()

    damage, health, armor = parse_stats(damage, health, armor)

    if dragon_type not in army.keys():
        army[dragon_type] = [[name, damage, health, armor]]
    else:
        for dragon_info in army[dragon_type]:
            if name == dragon_info[0]:
                dragon_info[1] = damage
                dragon_info[2] = health
                dragon_info[3] = armor
                break
        else:
            army[dragon_type].append([name, damage, health, armor])


for dragon_type, dragon_info in army.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    dragons = 0
    for name, damage, health, armor in dragon_info:
        total_damage += damage
        total_health += health
        total_armor += armor
        dragons += 1

    dragon_info = sorted(dragon_info)
    print(f'{dragon_type}::({total_damage/dragons:.2f}/{total_health/dragons:.2f}/{total_armor/dragons:.2f})')
    for name, damage, health, armor in dragon_info:
        print(f'-{name} -> damage: {damage}, health: {health}, armor: {armor}')

######### OR #########


def add_(dict_, color_, name_, dmg_, hp_, armor_):
 
    if dmg_ == "null":
        dmg_ = 45
    if hp_ == "null":
        hp_ = 250
    if armor_ == 'null':
        armor_ = 10
 
    dmg_ = int(dmg_)
    armor_ = int(armor_)
    hp_ = int(hp_)
 
    if color_ in dict_:
        dict_[color_][name_] = [dmg_, hp_, armor_]
    else:
        dict_[color_] = {name_: [dmg_, hp_, armor_]}
 
    return dict_
 
 
our_dict = {}
average_dict = {}
n = int(input())
for time in range(n):
    command = input()
    color, name, dmg, hp, armor = command.split()
    our_dict = add_(our_dict, color, name, dmg, hp, armor)
 
 
for colors, name_and_items in our_dict.items():
    average_dict[colors] = [0, 0, 0]
    for name, items in name_and_items.items():
        for index in range(len(items)):
            average_dict[colors][index] += int(our_dict[colors][name][index])
    average_dict[colors] = [f'{(average_dict[colors][0] / len(our_dict[colors])):.2f}',
                            f'{(average_dict[colors][1] / len(our_dict[colors])):.2f}', f'{(average_dict[colors][2] / len(our_dict[colors])):.2f}']
 
for color, massive in average_dict.items():
    print(f'{color}::({massive[0]}/{massive[1]}/{massive[2]})')
    for name, massive2 in sorted(our_dict[color].items(), key=lambda x: x[0]):
        print(
            f'-{name} -> damage: {massive2[0]}, health: {massive2[1]}, armor: {massive2[2]}')