collection_of_items = input().split("|")

budget = float(input())

new_prices = []
profit = 0

for item in collection_of_items:
    affordable = False

    product_name, product_price = item.split("->")

    product_price = float(product_price)

    if product_name == "Clothes" and product_price <= 50 and budget >= product_price:
        affordable = True

    elif product_name == "Shoes" and product_price <= 35 and budget >= product_price:
        affordable = True

    elif product_name == "Accessories" and product_price <= 20.50 and budget >= product_price:
        affordable = True

    if affordable:
        budget -= product_price
        new_price = product_price + (product_price * 0.40)
        new_prices.append(new_price)
        profit += product_price * 0.40

for new_price in new_prices:
    print(f"{new_price:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")

budget = budget + sum(new_prices)

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")



############ w/ function #############



def available(item_type, price):
    if item_type == 'Clothes' and price <= 50:
        return True
    elif item_type == 'Shoes' and price <= 35:
        return True
    elif item_type == 'Accessories' and price <= 20.50:
        return True


items = input().split('|')

budget = int(input())
savings = 0
profit = 0

for item in items:
    item_type, price = item.split('->')
    price = float(price)
    if available(item_type, price):
        if price <= budget:
            budget -= price
            profit += price * 0.4
            savings += price * 1.4
            print(f"{price*1.4:.2f}", end=' ')
savings += budget

print()
print(f"Profit: {profit:.2f}")

if savings >= 150:
    print("Hello, France!")
else:
    print("Time to go.")