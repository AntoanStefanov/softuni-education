eggs_in_stock = int(input())

command = input()
bought_eggs = 0
while command != "Close":

    eggs_bought_sold = int(input())
    if command == "Fill":
        eggs_in_stock += eggs_bought_sold

    elif command == "Buy":
        if eggs_in_stock < eggs_bought_sold:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_stock}.")
            break
        eggs_in_stock -= eggs_bought_sold
        bought_eggs += eggs_bought_sold
    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{bought_eggs} eggs sold.")
