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

############## SECOND TIME ############# 
box_of_clothes = [int(clothes) for clothes in input().split()]  # stack
one_rack_capacity = int(input())


clothes_on_current_rack = 0
racks = 0


while box_of_clothes:
    current_cloth = box_of_clothes.pop()
    clothes_on_current_rack += current_cloth
    if clothes_on_current_rack == one_rack_capacity:
        clothes_on_current_rack = 0
        racks += 1
    elif clothes_on_current_rack > one_rack_capacity:
        racks += 1
        clothes_on_current_rack = current_cloth

        
if clothes_on_current_rack:
    racks += 1


print(racks)
