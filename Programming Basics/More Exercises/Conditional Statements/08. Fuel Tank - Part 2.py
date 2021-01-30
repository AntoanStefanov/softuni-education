fuel = input()
liters = float(input())
discount_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

if discount_card == "Yes":
    if fuel == "Gasoline":
        gasoline -= 0.18
        price = liters * gasoline
    elif fuel == "Diesel":
        diesel -= 0.12
        price = liters * diesel
    elif fuel == "Gas":
        gas -= 0.08
        price = liters * gas
else:
    if fuel == "Gasoline":
        price = liters * gasoline
    elif fuel == "Diesel":
        price = liters * diesel
    elif fuel == "Gas":
        price = liters * gas

if 20 <= liters <= 25:
    price *= 92 / 100
elif liters > 25:
    price *= 90 / 100


print(f"{price:.2f} lv.")
