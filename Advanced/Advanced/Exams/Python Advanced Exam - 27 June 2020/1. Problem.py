from collections import deque


def enough_bombs(bombs_made):
    for bomb_made, count in bombs_made.items():
        if count < 3:
            return False
    return True


bombs_recipe = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120,
}

bombs_made = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]


while bomb_effects and bomb_casings:
    first_bomb_effect = bomb_effects.popleft()
    last_bomb_casing = bomb_casings.pop()

    mixed_sum = first_bomb_effect + last_bomb_casing

    for bomb, material_needed in bombs_recipe.items():
        if mixed_sum == material_needed:
            bombs_made[bomb] += 1
            break
    else:
        last_bomb_casing -= 5
        bomb_effects.appendleft(first_bomb_effect)
        bomb_casings.append(last_bomb_casing)

    if enough_bombs(bombs_made):
        break


if enough_bombs(bombs_made):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(i) for i in bomb_effects])}")
else:
    print("Bomb Effects: empty")


if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(i) for i in bomb_casings])}")
else:
    print("Bomb Casings: empty")

sorted_bombs = sorted(bombs_made.items(), key=lambda t: t[0])

for bomb_made, count in sorted_bombs:
    print(f"{bomb_made}: {count}")
