luggage_capacity = float(input())

command = input()
number_suitcases = 0

while command != "End":
    suitcase_capacity = float(command)
    number_suitcases += 1
    if number_suitcases % 3 == 0:
        suitcase_capacity += suitcase_capacity * 0.10
    luggage_capacity -= suitcase_capacity
    if luggage_capacity < 0:
        number_suitcases -= 1
        break

    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {number_suitcases} suitcases loaded.")
else:
    print("No more space!")
    print(f"Statistic: {number_suitcases} suitcases loaded.")
