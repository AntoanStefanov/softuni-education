targets = [int(value) for value in input().split()]
shot_targets = 0
while True:
    index = input()
    if index == "End":
        break
    index = int(index)
    if index < len(targets):
        if targets[index] != -1:
            value = targets[index]
            targets[index] = -1
            shot_targets += 1

        for index, target in enumerate(targets):
            if target != -1:
                if target > value:
                    targets[index] -= value
                else:
                    targets[index] += value


print(f"Shot targets: {shot_targets} -> ", end='')
for target in targets:
    print(f"{target} ", end='')
