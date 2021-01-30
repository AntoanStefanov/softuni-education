beverage = input()
sugar = input()
number_of_beverages = int(input())
price = 0
if beverage == "Espresso":
    if sugar == "Without":
        price = 90
    elif sugar == "Normal":
        price = 100
    elif sugar == "Extra":
        price = 120
elif beverage == "Cappuccino":
    if sugar == "Without":
        price = 100
    elif sugar == "Normal":
        price = 120
    elif sugar == "Extra":
        price = 160
elif beverage == "Tea":
    if sugar == "Without":
        price = 50
    elif sugar == "Normal":
        price = 60
    elif sugar == "Extra":
        price = 70
price = price * number_of_beverages
if sugar == "Without":
    price *= 0.65

if beverage == "Espresso" and number_of_beverages >= 5:
    price *= 0.75

if price > 1500:
    price *= 0.80

print(
    f"You bought {number_of_beverages} cups of {beverage} for {price/100:.2f} lv.")


######### OR ##########


beverage = input()
sugar = input()
number_of_beverages = int(input())
price = 0
if beverage == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20
elif beverage == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
elif beverage == "Tea":
    if sugar == "Without":
        price = 0.50
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70
price = price * number_of_beverages
if sugar == "Without":
    price *= 0.65

if beverage == "Espresso" and number_of_beverages >= 5:
    price *= 0.75

if price > 15:
    price *= 0.80

print(
    f"You bought {number_of_beverages} cups of {beverage} for {price:.2f} lv.")
