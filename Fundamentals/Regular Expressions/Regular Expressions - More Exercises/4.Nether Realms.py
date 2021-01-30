import re

demons_info = []
demons = input().split(',')
regex = r'[^0-9\.+\*\/\s\,-]'
# stackoverflow [+-]?([0-9]*[.])?[0-9]+   |  +/- integers and floats
pattern = r'(\+|-*?\d+\.?(\d+)?)?'
repattern = r'[\/\*]'
for demon in demons:

    demon = demon.strip()
    chars_for_health = re.findall(regex, demon)
    numbers_for_health = [ord(x) for x in chars_for_health]
    health = sum(numbers_for_health)

    digits_for_damage = re.finditer(pattern, demon)

    damage_list = []

    for match in digits_for_damage:
        if match.group():
            if match.group().isdigit():
                damage_list.append(int(match.group()))
            else:
                damage_list.append(float(match.group()))
    damage = sum(damage_list)

    operations = re.findall(repattern, demon)

    for operation in operations:
        if operation == '*':
            damage *= 2
        elif operation == '/':
            damage /= 2

    demons_info.append({'demon': demon, 'damage': damage, 'health': health})


sorted_demons_info = sorted(demons_info, key=lambda k: k['demon'])


for demon_dict in sorted_demons_info:
    print(
        f"{demon_dict['demon']} - {demon_dict['health']} health, {demon_dict['damage']:.2f} damage")


# https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
# Use GUI for graphical user interface.