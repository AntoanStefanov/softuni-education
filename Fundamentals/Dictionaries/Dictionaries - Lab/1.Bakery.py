elements = input().split()

bakery = {}

for index in range(0, len(elements), 2):
    product_name = elements[index]
    quantity = elements[index + 1]
    bakery[product_name] = int(quantity)

print(bakery)
