from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles_with_water = [int(bottle) for bottle in input().split()]

wasted_water = 0

while True:

    if not cups or not bottles_with_water:
        break

    current_bottle = bottles_with_water.pop()

    if current_bottle >= cups[0]:
        current_cup = cups.popleft()
        wasted_water += current_bottle - current_cup

    else:
        cups[0] -= current_bottle

if bottles_with_water:
    bottles_with_water.reverse()
    bottles_with_water = [str(bottle) for bottle in bottles_with_water]
    print(f"Bottles: {' '.join(bottles_with_water)}")
elif cups:
    cups = [str(cup) for cup in cups]
    print(f"Cups: {' '.join(cups)}")
print(f"Wasted litters of water: {wasted_water}")
