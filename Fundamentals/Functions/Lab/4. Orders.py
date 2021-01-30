def orders(product, quantity):
    price = None
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    if price is not None:
        return price * quantity


product = input()
price = float(input())

print(f"{orders(product, price):.2f}")
