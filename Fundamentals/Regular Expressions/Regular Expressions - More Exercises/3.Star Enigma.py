import re
n = int(input())


pattern = r'[star]'
all_decrypted_messages = []
for _ in range(n):
    encrypted_message = input()
    occurances = re.findall(pattern, encrypted_message, re.IGNORECASE)
    key = len(occurances)
    decrypted_message = ''
    for symbol in encrypted_message:
        decrypted_symbol = chr(ord(symbol) - key)
        decrypted_message += decrypted_symbol
    all_decrypted_messages.append(decrypted_message)

regex = r'(^|(?<=@))(?P<planet_name>[A-Za-z]+)[^@!\:>-]*:(?P<planet_population>\d+)[^@!\:>-]*?!(?P<attack_type>A|D)![^@!\:>-]*?\->(?P<soldier_count>\d+)'
attacked_planets = []
destroyed_planets = []
for message in all_decrypted_messages:

    info = re.finditer(regex, message)

    for match in info:

        attack_type = match['attack_type']
        planet = match.group('planet_name')
        if attack_type == 'A':
            attacked_planets.append(planet)
        elif attack_type == 'D':
            destroyed_planets.append(planet)


print(f'Attacked planets: {len(attacked_planets)}')

for planet in sorted(attacked_planets):
    print(f'-> {planet}')


print(f'Destroyed planets: {len(destroyed_planets)}')

for planet in sorted(destroyed_planets):
    print(f'-> {planet}')
