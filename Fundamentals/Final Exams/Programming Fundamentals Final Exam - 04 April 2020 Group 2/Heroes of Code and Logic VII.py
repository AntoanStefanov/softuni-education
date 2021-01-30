number_of_heroes = int(input())

heroes_hp = {}
heroes_mp = {}

for _ in range(number_of_heroes):

    hero_name, hp, mp = input().split()

    heroes_hp[hero_name] = int(hp)
    heroes_mp[hero_name] = int(mp)


while True:
    data = input().split(" - ")
    command = data[0]
    if command == "End":
        break
    hero_name = data[1]

    if command == "CastSpell":

        mp_needed = int(data[2])

        spell_name = data[3]

        if heroes_mp[hero_name] >= mp_needed:
            heroes_mp[hero_name] -= mp_needed
            print(
                f"{hero_name} has successfully cast {spell_name} and now has {heroes_mp[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes_hp[hero_name] -= damage
        if heroes_hp[hero_name] > 0:
            print(
                f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_hp[hero_name]} HP left!")
        else:
            heroes_hp.pop(hero_name)
            heroes_mp.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif command == "Recharge":
        amount = int(data[2])
        before_recharge = heroes_mp[hero_name]
        heroes_mp[hero_name] += amount
        if heroes_mp[hero_name] > 200:
            heroes_mp[hero_name] = 200
            print(f"{hero_name} recharged for {200 - before_recharge} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(data[2])
        before_heal = heroes_hp[hero_name]
        heroes_hp[hero_name] += amount
        if heroes_hp[hero_name] > 100:
            heroes_hp[hero_name] = 100
            print(f"{hero_name} healed for {100 - before_heal} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")

sorted_heroes = dict(sorted(heroes_hp.items(), key=lambda t: (-t[1], t[0])))

for hero in sorted_heroes:
    print(hero)
    print(f"  HP: {sorted_heroes[hero]}")
    print(f"  MP: {heroes_mp[hero]}")
	

