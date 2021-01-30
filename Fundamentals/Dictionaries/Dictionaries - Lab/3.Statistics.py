from collections import defaultdict

products = defaultdict(int)

while True:
    data = input()

    if data == "statistics":
        break

    product, quantity = data.split(": ")

    products[product] += int(quantity)


print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")


print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
