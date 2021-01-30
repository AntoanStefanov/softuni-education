detergent_bottles = int(input())
detergent_liquid = detergent_bottles * 750  # 1 bottle = 750 ml.
loading = 1
pots = 0
plates = 0
command = input()
while command != "End":
    dishes = int(command)
    if loading % 3 == 0:
        pots += dishes
        detergent_for_dishes = dishes * 15
    else:
        plates += dishes
        detergent_for_dishes = dishes * 5
    detergent_liquid -= detergent_for_dishes
    if detergent_liquid < 0:
        print(
            f"Not enough detergent, {abs(detergent_liquid)} ml. more necessary!")
        break
    loading += 1
    command = input()
else:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent_liquid} ml.")


############## OR ############

detergent_bottles = int(input())

detergent_liquid = detergent_bottles * 750  # 1 bottle = 750 ml.

loading = 1
pots = 0
plates = 0

command = input()

while command != "End":
    dishes = int(command)
    if loading % 3 == 0:
        pots += dishes
        dishes *= 15
    else:
        plates += dishes
        dishes *= 5
    detergent_liquid -= dishes
    if detergent_liquid < 0:
        print(
            f"Not enough detergent, {abs(detergent_liquid)} ml. more necessary!")
        break
    loading += 1
    command = input()
else:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent_liquid} ml.")
