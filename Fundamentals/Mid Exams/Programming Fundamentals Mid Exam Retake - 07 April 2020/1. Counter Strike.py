initial_energy = int(input())
line = input()
won_battle = 0
won = True
while line != "End of battle":
    distance = int(line)
    if initial_energy - distance >= 0:
        won_battle += 1
        if won_battle % 3 == 0 and won_battle != 0:
            initial_energy += won_battle
        initial_energy -= distance
    else:
        print(
            f"Not enough energy! Game ends with {won_battle} won battles and {initial_energy} energy")
        won = False
        break
    line = input()
if won:
    print(f"Won battles: {won_battle}. Energy left: {initial_energy}")
