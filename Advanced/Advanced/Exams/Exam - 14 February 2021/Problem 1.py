from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]
perfect_firework_show = False
fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

while True:
    if (not firework_effects) or (not explosive_power):
        break

    if firework_effects and firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power and explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    firework_effect = firework_effects.popleft()

    mixed_sum = firework_effect + explosive_power[-1]

    if mixed_sum % 3 == 0 and (not mixed_sum % 5 == 0):
        fireworks['Palm Fireworks'] += 1
        explosive_power.pop()
    elif mixed_sum % 5 == 0 and (not mixed_sum % 3 == 0):
        fireworks['Willow Fireworks'] += 1
        explosive_power.pop()
    elif mixed_sum % 5 == 0 and mixed_sum % 3 == 0:
        fireworks['Crossette Fireworks'] += 1
        explosive_power.pop()
    else:
        firework_effect -= 1
        firework_effects.append(firework_effect)

    for firework, count in fireworks.items():
        if count < 3:
            break
    else:
        perfect_firework_show = True
        break

if perfect_firework_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(
        f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(
        f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for firework, count in fireworks.items():
    print(f'{firework}: {count}')
