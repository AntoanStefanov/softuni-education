budget = float(input())
command = input()


product_count = 0
total_price = 0


while command != "Stop":  # или при заявка за купуване на продукт,
    # чиято стойност е по-висока от наличния бюджет :
    price_of_the_product = float(input())
    product_count += 1
    if product_count % 3 == 0:
        price_of_the_product /= 2
    if price_of_the_product > budget:
        break
    budget -= price_of_the_product
    total_price += price_of_the_product
    command = input()

if command == "Stop":
    print(f"You bought {product_count} products for {total_price:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {price_of_the_product - budget:.2f} leva!")
