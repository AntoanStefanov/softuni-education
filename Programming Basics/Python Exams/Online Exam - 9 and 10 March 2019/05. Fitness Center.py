number_of_clients = int(input())

back = 0
chest = 0
legs = 0
abdominals = 0
protein_shake = 0
protein_bar = 0


for client in range(1, number_of_clients + 1):
    action = input()

    if action == "Back":
        back += 1
    elif action == "Chest":
        chest += 1
    elif action == "Legs":
        legs += 1
    elif action == "Abs":
        abdominals += 1
    elif action == "Protein shake":
        protein_shake += 1
    elif action == "Protein bar":
        protein_bar += 1

training_clients = back + chest + legs + abdominals
buying_clients = protein_shake + protein_bar


training_clients_percent = (training_clients / number_of_clients) * 100
buying_clients_percent = (buying_clients / number_of_clients) * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abdominals} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{training_clients_percent:.2f}% - work out")
print(f"{buying_clients_percent:.2f}% - protein")
