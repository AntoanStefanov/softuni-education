n = int(input())
info = {}
for _ in range(n):
    name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    info[name] = {'hp': hp, 'mp': mp}

command = input()
while not command == "End":
    command = command.split("-")
    if command[0].strip() == "CastSpell":
        hero = command[1].strip()
        mp_needed = int(command[2].strip())
        spell = command[3].strip()
        if info[hero]['mp'] < mp_needed:
            print(f"{hero} does not have enough MP to cast {spell}!")
        else:
            info[hero]['mp'] -= mp_needed
            print(
                f"{hero} has successfully cast {spell} and now has {info[hero]['mp']} MP!")
    elif command[0].strip() == "TakeDamage":
        hero = command[1].strip()
        damage = int(command[2].strip())
        attacker = command[3].strip()
        if info[hero]['hp'] - damage <= 0:
            print(f"{hero} has been killed by {attacker}!")
            info.pop(hero)
        else:
            info[hero]['hp'] -= damage
            print(
                f"{hero} was hit for {damage} HP by {attacker} and now has {info[hero]['hp'] } HP left!")

    elif command[0].strip() == "Recharge":
        hero = command[1].strip()
        amount = int(command[2].strip())
        if info[hero]['mp'] + amount > 200:
            print(f"{hero} recharged for {200 - info[hero]['mp']} MP!")
            info[hero]['mp'] = 200
        else:
            info[hero]['mp'] += amount
            print(f"{hero} recharged for {amount} MP!")
    elif command[0].strip() == "Heal":
        hero = command[1].strip()
        amount = int(command[2].strip())
        if info[hero]['hp'] + amount > 100:
            print(f"{hero} healed for {100 -info[hero]['hp'] } HP!")
            info[hero]['hp'] = 100
        else:
            info[hero]['hp'] += amount
            print(f"{hero} healed for {amount} HP!")
    command = input()

for hero_name, stats in sorted(info.items(), key=lambda x: (-x[1]['hp'], x)):
    print(f'{hero_name}')
    print(f"HP: {stats['hp']}")
    print(f"MP: {stats['mp']}")
