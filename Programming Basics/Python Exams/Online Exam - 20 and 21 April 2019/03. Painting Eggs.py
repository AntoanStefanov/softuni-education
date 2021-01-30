eggs_size = input()
eggs_color = input()
number_of_batches = int(input())

if eggs_size == "Large":
    if eggs_color == "Red":
        price = 16
    elif eggs_color == "Green":
        price = 12
    elif eggs_color == "Yellow":
        price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        price = 13
    elif eggs_color == "Green":
        price = 9
    elif eggs_color == "Yellow":
        price = 7
elif eggs_size == "Small":
    if eggs_color == "Red":
        price = 9
    elif eggs_color == "Green":
        price = 8
    elif eggs_color == "Yellow":
        price = 5

total_price = number_of_batches * price
expenses = total_price * 0.35
print(f"{total_price - expenses:.2f} leva.")
