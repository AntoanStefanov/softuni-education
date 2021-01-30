fuel = input().lower()
liters = float(input())

if fuel == "diesel" or fuel == "gas" or fuel == "gasoline":
    if liters >= 25:
        print(f"You have enough {fuel}.")
    else:
        print(f"Fill your tank with {fuel}!")
else:
    print("Invalid fuel!")


#### OR #####

fuel = input()
liters = float(input())

if fuel == "Diesel" or fuel == "Gas" or fuel == "Gasoline":
    if liters >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")
