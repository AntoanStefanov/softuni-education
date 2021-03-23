box = [int(x) for x in input().split()]  # stack

rack_capacity = int(input())

racks = 0
clothes = 0

while box:
    cloth = box.pop()
    clothes += cloth
    if rack_capacity == clothes:
        racks += 1
        clothes = 0
    elif clothes > rack_capacity:
        box.append(cloth)
        clothes = 0
        racks += 1
    elif len(box) == 0:  # Когато попнем последната дреха е нужен рак също, иначе няма да се остави
        racks += 1
print(racks)
